"""
Emotion Recognition Service
Processes JPEG frames from browser and returns emotion analysis via JSON
"""
from flask import jsonify, request
import numpy as np
from deepface import DeepFace
from collections import deque
import base64
import io
from PIL import Image
import json
from datetime import datetime

# Store emotion history for temporal smoothing (per session)
global emotion_history
emotion_history = deque(maxlen=5)

# Emotion keys in consistent order
EMOTION_KEYS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]


def process_frame(frame):
    """
    Process a single frame and extract emotion data
    Returns emotion vector, bounding box, and dominant emotion
    """
    try:
        # Use DeepFace to analyze emotions
        pred = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        if isinstance(pred, list):
            face_data = pred[0]
        else:
            face_data = pred

        # Extract bounding box
        region = face_data["region"]
        bbox = {
            "x": region["x"],
            "y": region["y"],
            "w": region["w"],
            "h": region["h"]
        }

        # Extract emotion probabilities
        emotions = face_data["emotion"]

        # Convert to fixed-order vector
        emotion_vec = np.array([emotions[k] for k in EMOTION_KEYS])

        # Get dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        confidence = emotions[dominant_emotion]

        return {
            "success": True,
            "emotion_vector": emotion_vec.tolist(),
            "emotions": emotions,
            "dominant_emotion": dominant_emotion,
            "confidence": confidence,
            "bbox": bbox
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "emotions": {k: 0 for k in EMOTION_KEYS}
        }


def apply_temporal_smoothing(emotion_vec):
    """
    Apply temporal smoothing using a sliding window (like EEG processing)
    """
    emotion_history.append(emotion_vec)
    
    # Calculate mean across window
    smoothed = np.mean(list(emotion_history), axis=0)
    
    # Find dominant emotion
    dominant_idx = np.argmax(smoothed)
    dominant_emotion = EMOTION_KEYS[dominant_idx]
    confidence = smoothed[dominant_idx]
    
    return {
        "dominant_emotion": dominant_emotion,
        "confidence": float(confidence),
        "smoothed_emotions": {EMOTION_KEYS[i]: float(smoothed[i]) for i in range(len(EMOTION_KEYS))}
    }


# This will be imported and used by Flask app
def create_recognize_route(app):
    """
    Create the /recognize route in the Flask app
    Expects: POST with JPEG image data (base64 or raw bytes)
    Returns: JSON with emotion analysis
    """
    @app.route("/recognize", methods=["POST"])
    def recognize():
        """
        Endpoint: POST /recognize
        Body: JSON with 'image' field (base64-encoded JPEG)
        Response: JSON with emotion data and temporal smoothing
        """
        try:
            # Get image from request
            if "image" not in request.json:
                return jsonify({
                    "success": False,
                    "error": "No image provided"
                }), 400

            image_data = request.json["image"]

            # Decode base64 image
            if isinstance(image_data, str):
                # Remove data URL prefix if present
                if image_data.startswith("data:image"):
                    image_data = image_data.split(",")[1]
                
                image_bytes = base64.b64decode(image_data)
            else:
                image_bytes = image_data

            # Convert bytes to numpy array
            image = Image.open(io.BytesIO(image_bytes))
            frame = np.array(image)

            # Process frame
            result = process_frame(frame)

            if result["success"]:
                # Apply temporal smoothing
                smoothing_result = apply_temporal_smoothing(np.array(result["emotion_vector"]))
                result.update(smoothing_result)
                
                # Add timestamp
                result["timestamp"] = datetime.now().isoformat()

            return jsonify(result)

        except Exception as e:
            return jsonify({
                "success": False,
                "error": f"Processing error: {str(e)}"
            }), 500

    return recognize
