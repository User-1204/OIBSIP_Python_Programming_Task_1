# Voice Assistant

## Overview
This project is a modular, voice-activated assistant built in Python.  
It listens to your commands, responds by speaking, and can handle tasks like answering questions, checking the weather, searching the web, setting reminders, and sending emails. It demonstrates how speech recognition, text-to-speech, NLP, and external APIs can work together in a practical application.


## Features
- Understands and responds to your voice commands.
- Greets you based on the time of day.
- Provides real-time weather information.
- Answers "who is" or "what is" questions from Wikipedia.
- Opens common websites and searches Google.
- Sets reminders after asking what and when.
- Sends emails by asking for recipient, subject, and message.
- Handles casual conversation like greetings and thanks.


## Project Structure
| File / Module          | Purpose                                                                          |
|------------------------|----------------------------------------------------------------------------------|
| `main.py`              | Main script that listens, decides, and routes commands.                          |
| `modules/speech.py`    | Handles speaking and listening (speech-to-text and text-to-speech).              |
| `modules/weather.py`   | Fetches weather data and extracts city names.                                    |
| `modules/web.py`       | Opens sites or searches the web.                                                 |
| `modules/knowledge.py` | Answers general questions by calling Wikipedia.                                  |
| `modules/reminder.py`  | Sets and cancels reminders.                                                      |
| `modules/email.py`     | Sends emails using SMTP and saved credentials.                                   |
| `id.env`               | Stores API keys and email credentials (not included in version control).         |


## How it works
1. Captures your voice using speech recognition.
2. Detects keywords or phrases to decide what you asked for.
3. Calls a module to process your request.
4. Replies using text-to-speech while printing the response.
5. Keeps listening for your next command.


## Theory Behind the Assistant

### 1. Speech Recognition
Uses the `speech_recognition` library with Google's API to convert spoken words into text. It listens through your microphone and adjusts for ambient noise.

### 2. Text-to-Speech
Uses `pyttsx3` for voice responses, which runs offline and allows adjusting voice and speed for a calm tone.

### 3. Natural Language Processing
Uses `spaCy` to extract entities like city names, so queries like “How’s the weather in Delhi today?” work naturally.

### 4. Weather Integration
Uses Tomorrow.io’s API to get real-time weather by city name, decoding weather codes to human-friendly descriptions.

### 5. Knowledge Lookup
Fetches summaries from Wikipedia for “Who is…” or “What is…” questions, with fallback if data isn’t found.

### 6. Email Sending
Uses Python’s `smtplib` and `email.message`, pulling credentials securely from `.env`. Supports Gmail SSL and app passwords.

### 7. Reminder Scheduling
Uses `schedule` to set reminders in minutes. The assistant announces reminders when the time is up.

### 8. Web Interaction
Opens websites like YouTube or Google, or performs searches for other queries.


## Technologies Used
- Python 3.x
- pyttsx3
- SpeechRecognition
- requests
- spacy
- schedule
- smtplib and email
- dotenv
- webbrowser


## Setup and Installation
1. Create a `.env` file:
```

TOMORROW_API_KEY=your_api_key
EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_email_password

```
2. Folder structure
```

Assistant/
├── main.py
├── id.env
├── requirements.txt
└── modules/
    ├── speech.py
    ├── weather.py
    ├── web.py
    ├── knowledge.py
    ├── reminder.py
    └── email.py

```


## Running the Assistant
Navigate to your project folder and run:
```

python main.py

```

The assistant will greet you and wait for your voice commands.  
It also prints what you say and what it replies.


## Outcome and Demo
A demo video showing the project:

https://www.linkedin.com/posts/sakshii125_oasisinfobyte-internship-pythonprogramming-activity-7354023984478187520-R5Wq?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFlzQCEBcgHpQxLz_XBWlVGbkhDirbT-r5Y


## Known Issues
- Email may not work if Gmail blocks login; app passwords or less secure access may be needed.
- Speech recognition accuracy depends on microphone quality and accent.
- Wikipedia may not return results for uncommon topics.
- Reminders are only in minutes and don’t persist if the program restarts.


## Contributing
This project can be improved further:
- Smart home integration via MQTT.
- Offline Q&A modules.
- Multilingual support.
- GUI with PyQt or Tkinter.
- Better NLP for natural time parsing.

Pull requests and suggestions are welcome.
