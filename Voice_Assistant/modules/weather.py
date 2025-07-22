# Import required libraries
import requests, os, spacy, logging    # For API calls, environment variables, NLP, and error logging
from dotenv import load_dotenv     # To load API key securely from .env file
from modules.speech import speak, get_voice_input # For voice interaction functions

# Load environment variables from 'id.env'
load_dotenv("id.env")
API_KEY = os.getenv("TOMORROW_API_KEY")  # Get the weather API key
nlp = spacy.load("en_core_web_sm")  # Load spaCy NLP model for entity recognition

# Function to process voice command and provide weather info
def get_weather(command):
    city = ""                                     

    try:
        # Use NLP to extract a city from the spoken command
        doc = nlp(command)
        for ent in doc.ents:
            if ent.label_ == "GPE":   # GPE stands for geopolitical entity (like cities)
                city = ent.text
                break
    except Exception as e:
        logging.error(f"NLP error: {e}")           

    # If city wasn't detected, ask user again
    if not city:
        city = get_voice_input("Which city are you asking about?")
    if not city:
        speak("I still couldn't get the city name.")
        return

    try:
        # Make API call to fetch real-time weather for the city
        url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={API_KEY}"
        data = requests.get(url).json()["data"]["values"]  # Parse response
        
        temp = data.get("temperature")                     
        code = data.get("weatherCode")                    
        # Map weather codes to descriptive text
        descriptions = {
            1000: "Clear", 1001: "Cloudy", 1100: "Mostly Clear", 1101: "Partly Cloudy", 1102: "Mostly Cloudy",
            4000: "Drizzle", 4001: "Rain", 4200: "Light Rain", 4201: "Heavy Rain",
            5000: "Snow", 5100: "Light Snow", 5001: "Flurries", 5101: "Heavy Snow", 8000: "Thunderstorm",
            2100: "Light Fog", 2101: "Fog", 2102: "Heavy Fog", 4202: "Moderate Rain", 4203: "Heavy Drizzle",
            6200: "Freezing Rain", 7000: "Windy"
        }
        desc = descriptions.get(code)                     
        if not desc:
            desc = f"an unrecognized condition (code: {code})"

        # Speak out the weather information
        speak(f"It's {temp}°C with {desc} in {city}.")
    except Exception as e:
        logging.error(f"Weather fetch error: {e}")         
        speak("Sorry, I couldn't get weather info right now.")  