from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)

# In-memory storage (replace with database in production)
emotions = []
tasks = []

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
    global emotions
    
    if request.method == 'POST':
        data = request.json
        emotion_entry = {
            'emoji': data['emoji'],
            'timestamp': datetime.now().isoformat(),
            'id': len(emotions)
        }
        emotions.append(emotion_entry)
        return jsonify(emotion_entry)
    
    return jsonify(emotions)

@app.route('/api/tasks', methods=['GET', 'POST'])
def handle_tasks():
    global tasks
    
    if request.method == 'POST':
        data = request.json
        task_entry = {
            'title': data['title'],
            'start': data['start'],
            'end': data['end'],
            'id': len(tasks)
        }
        tasks.append(task_entry)
        return jsonify(task_entry)
    
    return jsonify(tasks)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

