# CareConnect - Emotion Tracking System

A web-based emotion tracking and caregiving coordination platform that bridges the communication gap between care recipients and their caregivers through intuitive emotion sharing and calendar management.

## Project Overview

CareConnect enables care recipients to express their emotional state through simple emoji selections, which are automatically shared with their caregivers via an integrated calendar system. This allows caregivers to monitor emotional wellbeing alongside daily tasks without requiring direct verbal communication from the recipient.

## Key Features

### For Recipients
- **Simple Emotion Selection**: Choose from 5 emoji options to express current feelings
  - 😊 Happy
  - 😢 Sad
  - 😰 Anxious
  - 😡 Angry
  - 😴 Tired
- **Submission History**: View timestamped log of all emotional check-ins
- **Clean Interface**: Minimal, distraction-free design for ease of use

### For Caregivers
- **Calendar Dashboard**: Full week view (Monday-Sunday) with 24-hour time slots
- **Automatic Emotion Blocks**: Recipient emotions appear as 30-minute calendar events
- **Task Management**: Click-to-add task scheduling system similar to Google Calendar
- **Real-time Updates**: Automatic refresh to display new emotions and tasks
- **Edit & Delete**: Modify or remove tasks as needed

### Navigation
- **Dual-Tab System**: Seamlessly switch between Recipient and Caregiver views
- **Role Selection**: Professional home page for initial role selection
- **Persistent Access**: Easy navigation between all pages

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Data Storage**: In-memory (can be extended to database)
- **Architecture**: RESTful API design

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation & Setup

### 1. Clone or Download the Project

```bash
git clone <your-repository-url>
cd careconnect
```

### 2. Create Project Structure

Organize your files as follows:

```
careconnect/
├── app.py
├── README.md
└── templates/
    ├── home.html
    ├── recipient.html
    └── caregiver.html
```

### 3. Install Dependencies

```bash
pip install flask
```

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
   - Click on an emoji that represents your current feeling
   - Press "Submit Feeling" button
   - View your submission appear in the history below
   - Your emotion will automatically appear on the caregiver's calendar

3. **As a Caregiver**:
   - View the weekly calendar dashboard
   - See recipient emotions appear as pink gradient blocks (30-minute duration)
   - Click any empty time slot to add a task
   - Enter task name and start time, then save
   - Click existing tasks to edit or delete them

### Switching Views

Use the navigation tabs at the top of any page to switch between Recipient and Caregiver views instantly.

## API Endpoints

### Emotions

**GET** `/api/emotions`
- Returns all emotion submissions
- Response: Array of emotion objects

**POST** `/api/emotions`
- Submit a new emotion
- Body: `{ "emoji": "😊" }`
- Response: Created emotion object with timestamp

### Tasks

**GET** `/api/tasks`
- Returns all tasks
- Response: Array of task objects

**POST** `/api/tasks`
- Create a new task
- Body: `{ "title": "Task Name", "start": "ISO datetime", "end": "ISO datetime" }`
- Response: Created task object

**DELETE** `/api/tasks/<task_id>`
- Delete a specific task
- Response: Success confirmation

## Design Philosophy

- **Minimalist Interface**: Reduces cognitive load for recipients who may be experiencing distress
- **Automatic Synchronization**: 5-second auto-refresh ensures caregivers receive timely updates
- **Visual Distinction**: Different gradient colors distinguish tasks (purple) from emotions (pink)
- **Accessibility-First**: Large touch targets and clear visual hierarchy
- **Professional Aesthetics**: Modern gradient designs with smooth transitions

## Current Limitations

- **Data Persistence**: Uses in-memory storage; data resets on server restart
- **Single User**: Designed for one recipient-caregiver pair
- **No Authentication**: No user login system implemented
- **Same Network**: Best used on the same local network

## Future Enhancements

- Database integration (PostgreSQL/SQLite) for persistent storage
- User authentication and multi-user support
- Mobile-responsive optimizations
- Push notifications for new emotions
- Data analytics and emotion trend visualization
- Export functionality for reports
- Customizable emotion options
- Recurring task support

## Contributing

This is a prototype project. To contribute:

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

## Acknowledgments

- Designed for caregivers and care recipients who need better emotional communication tools
- Inspired by the need for non-verbal emotional expression in caregiving relationships

---

**Built with ❤️ for better caregiving communication**
