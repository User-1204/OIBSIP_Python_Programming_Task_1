# Import required libraries
import requests  # For making API requests to Wikipedia
from modules.speech import speak  # To read out the response using text-to-speech

# Function to answer general queries 
def answer_general_query(command):
    try:
        # Extract the topic from the voice command
        topic = command.replace("who is", "").replace("what is", "").strip()

        # Build the API URL for Wikipedia summary
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

        # Send request and parse response as JSON
        response = requests.get(url).json()

        # If the response has a summary extract, speak it out
        if "extract" in response:
            speak(response["extract"])
        else:
            speak(f"I couldn’t find info on {topic}.")
    except Exception:
        speak("I'm having trouble accessing that info right now.")
