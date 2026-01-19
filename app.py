from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import json
import os
import sys
import threading

# Import emotion recognition service
from face import create_recognize_route
from physiological_stub import physiological_monitor

app = Flask(__name__)

# Face recognition state
face_recognition_running = False
face_recognition_thread = None
face_recognition_logs = []

# Initialize the /recognize endpoint
create_recognize_route(app)

# In-memory storage (replace with database in production)
emotions = []
tasks = []
emotion_id_counter = 0
task_id_counter = 0

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recipient')
def recipient():
    return render_template('recipient.html')

@app.route('/caregiver')
def caregiver():
    return render_template('caregiver.html')

@app.route('/api/emotions', methods=['GET', 'POST'])
def handle_emotions():
    global emotions, emotion_id_counter
    
    if request.method == 'POST':
        data = request.json
        emotion_entry = {
            'emoji': data['emoji'],
            'dominant_emotion': data.get('dominant_emotion', 'unknown'),
            'emotion_frames': data.get('emotion_frames', []),
            'heart_rate': data.get('heart_rate', physiological_monitor.get_current_heart_rate()),
            'timestamp': datetime.now().isoformat(),
            'id': emotion_id_counter
        }
        emotion_id_counter += 1
        emotions.append(emotion_entry)
        return jsonify(emotion_entry)
    
    return jsonify(emotions)

@app.route('/api/emotion-history', methods=['GET'])
def get_emotion_history():
    """Get the current emotion history from face.py"""
    try:
        # Try to import and access the emotion_history from face.py
        import sys
        import importlib.util
        spec = importlib.util.spec_from_file_location("face", os.path.join(os.path.dirname(__file__), 'face.py'))
        face_module = importlib.util.module_from_spec(spec)
        # Note: This won't work as face.py runs the main loop. 
        # Instead, we'll rely on the client-side to fetch this data
        return jsonify({'error': 'History tracking not available from this endpoint'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/tasks', methods=['GET', 'POST'])
def handle_tasks():
    global tasks, task_id_counter
    
    if request.method == 'POST':
        data = request.json
        task_entry = {
            'title': data['title'],
            'start': data['start'],
            'end': data['end'],
            'id': task_id_counter
        }
        task_id_counter += 1
        tasks.append(task_entry)
        return jsonify(task_entry)
    
    return jsonify(tasks)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'success': True})

@app.route('/api/emotions/<int:emotion_id>', methods=['DELETE'])
def delete_emotion(emotion_id):
    global emotions
    emotions = [e for e in emotions if e['id'] != emotion_id]
    return jsonify({'success': True})

@app.route('/api/physiological/<int:emotion_id>', methods=['GET'])
def get_physiological_data(emotion_id):
    """Get physiological data for a specific emotion entry"""
    global physiological_data
    
    if emotion_id in physiological_data:
        return jsonify(physiological_data[emotion_id])
    
    # If no data exists, generate it
    trend = physiological_monitor.get_heart_rate_trend(30)
    stats = physiological_monitor.get_heart_rate_stats(trend)
    
    physiological_data[emotion_id] = {
        'heart_rate': physiological_monitor.get_current_heart_rate(),
        'trend': trend,
        'stats': stats
    }
    
    return jsonify(physiological_data[emotion_id])

@app.route('/api/physiological/current', methods=['GET'])
def get_current_physiological():
    """Get current physiological readings"""
    heart_rate = physiological_monitor.get_current_heart_rate()
    
    return jsonify({
        'heart_rate': heart_rate,
        'timestamp': datetime.now().isoformat(),
        'status': 'normal' if 60 <= heart_rate <= 100 else 'elevated' if heart_rate > 100 else 'low'
    })

@app.route('/api/heart_rate', methods=['GET'])
def get_heart_rate():
    """
    Endpoint: GET /api/heart_rate
    Returns: JSON with current heart rate
    """
    heart_rate = physiological_monitor.get_current_heart_rate()
    return jsonify({'heart_rate': heart_rate})

# Face Recognition Endpoints
@app.route('/api/face-recognition/start', methods=['POST'])
def start_face_recognition():
    """Start the face recognition camera"""
    global face_recognition_running, face_recognition_logs
    
    # Always allow starting, even if already running (just restart it)
    face_recognition_running = True
    face_recognition_logs.append({
        'timestamp': datetime.now().isoformat(),
        'message': 'Face recognition started'
    })
    
    return jsonify({
        'success': True,
        'message': 'Face recognition started',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/face-recognition/stop', methods=['POST'])
def stop_face_recognition():
    """Stop the face recognition camera"""
    global face_recognition_running, face_recognition_logs
    
    # Always allow stopping
    face_recognition_running = False
    face_recognition_logs.append({
        'timestamp': datetime.now().isoformat(),
        'message': 'Face recognition stopped'
    })
    
    return jsonify({
        'success': True,
        'message': 'Face recognition stopped',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/face-recognition/status', methods=['GET'])
def face_recognition_status():
    """Get the current status of face recognition"""
    global face_recognition_running
    
    return jsonify({
        'running': face_recognition_running,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/face-recognition/logs', methods=['GET'])
def get_face_recognition_logs():
    """Get face recognition logs"""
    global face_recognition_logs
    
    # Keep only last 100 logs
    logs = face_recognition_logs[-100:]
    
    return jsonify({
        'logs': logs,
        'total': len(face_recognition_logs),
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

