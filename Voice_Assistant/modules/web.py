# Import required libraries
import webbrowser   # Used to open websites in the default browser
from modules.speech import speak  # Used for assistant's voice responses

# Function to open a website based on voice command
def open_site(command):
    # Dictionary mapping keywords to popular websites
    sites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "wikipedia": "https://wikipedia.org",
        "news": "https://news.google.com",
        "instagram": "https://instagram.com",
        "twitter": "https://twitter.com",
        "linkedin": "https://linkedin.com",
        "github": "https://github.com",
        "spotify": "https://spotify.com"
    }

    # Loop through sites and check if any keyword is present in the command
    for key, url in sites.items():
        if key in command:
            webbrowser.open(url)          
            speak(f"Opening {key} now.")      
            return

    # If keyword does not match, ask the user again
    speak("Tell me which website you'd like to open.")

# Function to perform a general Google search
def search_web(command):
    # Clean up the command to extract the search query
    query = command.replace("search", "").replace("find", "").strip()

    # If query is not empty, perform Google search
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}.")     
    else:
        speak("What would you like me to search for?")  