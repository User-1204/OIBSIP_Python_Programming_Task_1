# Import necessary libraries
import pyttsx3   # For text-to-speech conversion
import speech_recognition as sr  # For capturing and converting speech to text
import logging    # For error logging

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set voice
voices = engine.getProperty('voices')
for voice in voices:
    if "male" in voice.name.lower() or "male" in voice.id.lower():
        engine.setProperty("voice", voice.id)
        break

# Set speaking rate for better delivery
engine.setProperty("rate", 160)

# Function to convert text to speech and speak it out loud
def speak(text):
    print(f"Assistant: {text}")  
    try:
        engine.say(text)        
        engine.runAndWait()      
    except Exception as e:
        logging.error(f"Speech error: {e}")  # Log any speech synthesis error

# Function to capture and convert user's voice input into text
def get_voice_input(prompt=None):
    recognizer = sr.Recognizer()     
    with sr.Microphone() as source: 
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Calibrate for background noise
        if prompt:
            speak(prompt)          
        try:
            # Listen for speech input with timeout settings
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio).lower()  # Convert audio to text
            print(f"You: {command}")  
            return command
        except sr.WaitTimeoutError:
            speak("Listening timed out.")  
        except sr.UnknownValueError:
            speak("I couldn't understand. Could you repeat?")  
        except sr.RequestError as e:
            speak("Speech service is down. Try again later.")  
            logging.error(f"Request error: {e}")
        return ""  # Return empty string if recognition failed
