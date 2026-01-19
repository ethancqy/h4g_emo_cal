# CareConnect - Comprehensive Emotion & Health Tracking System

A web-based emotion tracking and caregiving coordination platform that bridges the communication gap between care recipients and their caregivers through intuitive emotion sharing, **facial emotion recognition**, **heart rate monitoring**, and calendar management.

## Problem Statement
Develop a solution that improve relationships between caregiver and the care recipient so that caregivers can provide the care that the care recipients want/need in a mutually respectful, meaningful, and joyful way?

## Project Overview

CareConnect enables care recipients to express their emotional state through multiple channels: manual emoji selection, automated facial emotion detection, and physiological monitoring via Fitbit integration. All data is automatically shared with caregivers through an integrated calendar system, allowing comprehensive wellbeing monitoring without requiring constant verbal communication.

## Key Features

![Home Page](https://github.com/ethancqy/h4g_emo_cal/blob/main/photos/home.png)

### For Recipients
- **Multiple Emotion Input Methods**:
  - **Manual Selection**: Choose from 5 emoji options to express current feelings
    - 😊 Happy
    - 😢 Sad
    - 😰 Anxious
    - 😡 Angry
    - 😴 Tired
  - **Facial Recognition**: Real-time emotion detection using webcam and computer vision
  - **Heart Rate Tracking**: Continuous monitoring via Fitbit integration (currently simulated)
- **Submission History**: View timestamped log of all emotional check-ins with source indication
- **Privacy Controls**: Opt-in for facial recognition and biometric tracking
- **Clean Interface**: Minimal, distraction-free design for ease of use

![Recipient Page](https://github.com/ethancqy/h4g_emo_cal/blob/main/photos/recipient.png)

### For Caregivers
- **Calendar Dashboard**: Full week view (Monday-Sunday) with 24-hour time slots
- **Automatic Emotion Blocks**: Recipient emotions appear as 30-minute calendar events
- **Multi-Source Data**: View emotions from manual input, facial recognition, and physiological data
- **Task Management**: Click-to-add task scheduling system similar to Google Calendar
- **Real-time Updates**: Automatic refresh to display new emotions and tasks
- **Health Insights**: Monitor heart rate patterns alongside emotional states
- **Edit & Delete**: Modify or remove tasks as needed

![Caregiver Page](https://github.com/ethancqy/h4g_emo_cal/blob/main/photos/caregiver.png)

### Advanced Monitoring
- **Facial Emotion Recognition**:
  - Real-time face detection and emotion analysis
  - Supports 7 emotion categories (happy, sad, angry, surprise, fear, disgust, neutral)
  - Privacy-first: processing happens locally, no images stored
  - Confidence scoring for accuracy assessment

- **Heart Rate Monitoring**:
  - Continuous Fitbit integration (Currently simulated)
  - Resting heart rate tracking

### Navigation
- **Dual-Tab System**: Seamlessly switch between Recipient and Caregiver views
- **Role Selection**: Professional home page for initial role selection
- **Persistent Access**: Easy navigation between all pages

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Computer Vision**: OpenCV, DeepFace
- **Machine Learning**: TensorFlow/Keras for emotion detection
- **Biometric Integration**: Fitbit API (in development)
- **Data Storage**: In-memory (can be extended to database)
- **Architecture**: RESTful API design

## Prerequisites

- Python 3.11.14.
- pip (Python package manager)
- Webcam (for facial emotion recognition)

## Installation & Setup

### 1. Clone or Download the Project

```bash
git clone https://github.com/ethancqy/h4g_emo_cal
cd h4g_emo_cal
```

### 2. Create Project Structure

Organize your files as follows:

```
h4g_emo_cal/
├── app.py
├── face.py
├── physiological_stub.py
├── requirements.txt
├── README.md
└── templates/
    ├── home.html
    ├── recipient.html
    └── caregiver.html
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:
- Flask - Web framework
- opencv-python - Computer vision and facial detection
- deepface - Facial emotion recognition
- tensorflow - Deep learning backend
- numpy - Numerical computing
- fitbit - Fitbit API integration (optional)

### 4. Run the Application

```bash
python app.py
```

### 5. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage Guide

### Getting Started

1. **Choose Your Role**: On the home page, select either "I'm a Recipient" or "I'm a Caregiver"

2. **As a Recipient**:
   
   **Manual Emotion Entry**:
   - Click on an emoji that represents your current feeling
   - Press "Submit Feeling" button
   - View your submission appear in the history below
   
   **Facial Emotion Recognition**:
   - Click "Enable Camera" to start facial recognition
   - Allow browser camera permissions when prompted
   - The system will automatically detect and log your emotions
   - Current emotion and confidence level displayed in real-time
   - Click "Stop Camera" to disable recognition
   
   **Heart Rate Monitoring**:
   - Heart-Rate tracking automatically occurs
   - Captured concurrently with "Submit Feeling" button
   
   All emotions automatically appear on the caregiver's calendar

3. **As a Caregiver**:
   - View the weekly calendar dashboard
   - See recipient emotions appear as colored gradient blocks
   - Click any empty time slot to add a task
   - Enter task name and start time, then save
   - Click existing tasks/emotions to view details
   - Monitor patterns and trends over time

### Switching Views

Use the navigation tabs at the top of any page to switch between Recipient and Caregiver views instantly.

## API Endpoints

### Tasks

**GET** `/api/tasks`
- Returns all tasks from the caregiver calendar
- Response: ```[{
  "id": 0,
  "title": "Morning Routine",
  "start": "2026-01-19T08:00:00",
  "end": "2026-01-19T09:00:00"
}]```

**POST** `/api/tasks`
- Create a new task on the caregiver calendar
- Response: ```{
  "title": "Task Name",
  "start": "2026-01-19T08:00:00",
  "end": "2026-01-19T09:00:00"
}```

**DELETE** `/api/tasks/<task_id>`
- Delete a specific task.
- Response: ```{"success": true}```

### Emotions

**GET** `/api/emotions`
- Returns all emotion submissions
- Response: ```[{
  "id": 0,
  "emoji": "😊",
  "dominant_emotion": "happy",
  "emotion_frames": [...],
  "heart_rate": 72,
  "timestamp": "2026-01-19T12:34:56.789"
}]```

**POST** `/api/emotions`
- Submit a new emotion with facial recognition data and heart rate
- Response: ```{
  "emoji": "😊",
  "dominant_emotion": "happy",
  "emotion_frames": [...],
  "heart_rate": 72
}```

**DELETE** `/api/emotions/<emotion_id>`
- Delete a specific emotion entry
- Response: ```{
  "success": true
}```

### Heart-Rate Monitoring

**GET** `/api/heartrate`
- Returns current simulated heart rate
- Response: ```{
  "heart_rate": 72
}```

**GET** `api/physiological/current`
- Returns current physiological readings with status
- Response: ```{
  "heart_rate": 72,
  "timestamp": "2026-01-19T12:34:56.789",
  "status": "normal"
}```

**GET** `/api/physiological/<emotion_id>`
- Get physiological data for a specific emotion entry
- Response: ```{
  "heart_rate": 72,
  "trend": [...],
  "stats": {...}
}```

### Face Recognition

**POST** `/recognize`
- Submit image for facial emotion recognition (created by face.py module)
- Response: ```{
  "success": true,
  "dominant_emotion": "happy",
  "confidence": 0.95,
  "emotions": {...},
  "bbox": {...}
}```

**POST** '/api/face-recognition/start`
- Start face recognition monitoring
- Response: ```{
  "success": true,
  "message": "Face recognition started",
  "timestamp": "2026-01-19T12:34:56.789"
}```

**POST** `/api/face-recognition/stop`
- Stop face recognition monitoring
- Response: ```{
  "success": true,
  "message": "Face recognition stopped",
  "timestamp": "2026-01-19T12:34:56.789"
}```

**GET** `/api/face-recognition/status`
- Get face recognition activity log (last 100 entries)
- Response: ```{
  "logs": [...],
  "total": 150,
  "timestamp": "2026-01-19T12:34:56.789"
}```

## Technical Implementation

### Facial Emotion Recognition (`face.py`)

The facial emotion recognition module uses:
- **OpenCV**: Real-time face detection from webcam feed
- **DeepFace**: Pre-trained neural network for emotion classification
- **Processing Pipeline**:
  1. Capture video frame from webcam
  2. Detect faces using Haar Cascade classifier
  3. Extract face region and preprocess
  4. Run emotion prediction model
  5. Return dominant emotion with confidence score
  6. Submit to API for caregiver notification

### Heart Rate Integration (`physiological_stub.py`) - In Development

The Fitbit integration will:
- Authenticate with Fitbit OAuth 2.0
- Poll for heart rate data at configurable intervals
(Currently simulated)

## Design Philosophy

- **Multi-Modal Input**: Accommodates different communication preferences and abilities
- **Passive Monitoring**: Facial and heart rate tracking require minimal active participation
- **Privacy-First**: All facial processing happens locally; no images transmitted or stored
- **Minimalist Interface**: Reduces cognitive load for recipients experiencing distress
- **Automatic Synchronization**: Real-time updates ensure caregivers receive timely information
- **Visual Distinction**: Different gradient colors distinguish tasks and emotion sources
- **Accessibility-First**: Large touch targets and clear visual hierarchy
- **Professional Aesthetics**: Modern gradient designs with smooth transitions

## Privacy & Security

- **Local Processing**: Facial emotion recognition runs entirely on the user's device
- **No Image Storage**: Webcam frames are processed and immediately discarded
- **Consent-Based**: All monitoring features require explicit user activation
- **Data Minimization**: Only emotion classifications and metadata are transmitted
- **Fitbit Authorization**: Secure OAuth flow for health data access
- **Optional Features**: Users can choose which monitoring methods to enable

## Current Limitations

- **Data Persistence**: Uses in-memory storage; data resets on server restart
- **Single User**: Designed for one recipient-caregiver pair
- **No Authentication**: No user login system implemented
- **Network Dependency**: Requires local network or port forwarding for remote access
- **Facial Recognition**: Requires good lighting and clear face visibility
- **Browser Compatibility**: Webcam access requires modern browser with camera permissions

## Future Enhancements

### Infrastructure
- Database integration (PostgreSQL/SQLite) for persistent storage
- User authentication and multi-user support
- Cloud deployment for remote access
- Mobile applications (iOS/Android)

### Features
- Advanced emotion analytics and trend visualization
- Machine learning for pattern detection and predictions
- Export functionality for medical reports
- Customizable emotion categories and thresholds
- Recurring task support
- Family/team caregiver coordination
- Integration with other health devices (Apple Watch, smart scales)
- Voice-based emotion detection
- Medication reminders correlated with emotional states
- Emergency alert system for concerning patterns

### Intelligence
- AI-powered caregiver recommendations
- Predictive modeling for emotional episodes
- Natural language processing for journaling
- Correlation analysis between activities and emotions

## Troubleshooting

### Webcam Issues
- Ensure browser has camera permissions enabled
- Check that no other application is using the webcam
- Verify webcam drivers are up to date
- Try a different browser (Chrome/Firefox recommended)

### Dependency Errors
- Ensure all requirements are installed: `pip install -r requirements.txt`
- For TensorFlow issues, may need to install specific version for your OS
- OpenCV may require additional system libraries on Linux

### Performance
- Facial recognition requires decent CPU/GPU
- Consider reducing frame rate if system is slow
- Close unnecessary applications

## Contributing

This is an active development project. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For questions, issues, or feedback:
- Open an issue in the repository
- Contact the development team
- Check documentation wiki

## Acknowledgments

- Designed for caregivers and care recipients who need better emotional communication tools
- Inspired by the need for non-verbal emotional expression in caregiving relationships
- Built with computer vision and machine learning for passive wellbeing monitoring
- Special thanks to the DeepFace and OpenCV communities

## Citations & References

- DeepFace: Facial emotion recognition framework
- OpenCV: Computer vision library
- Fitbit API: Health data integration
- Flask: Web application framework

---

**Built with ❤️ for better caregiving communication**

*Empowering caregivers with real-time emotional and physiological insights*
