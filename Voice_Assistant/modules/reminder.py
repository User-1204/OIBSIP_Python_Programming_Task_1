# Import required libraries
import schedule    # For scheduling timed tasks
from modules.speech import speak  # For assistant voice responses

# Function to set a reminder after a given number of minutes
def set_reminder(text, minutes):
    try:
        # Define the task that will run after the timer
        def reminder_task(text=text):
            speak(f"Reminder: {text}")   # Speak the reminder messages
        
        # Schedule the reminder task to run after 'minutes' interval
        schedule.every(minutes).minutes.do(reminder_task).tag(f"reminder_{text}")
        
        # Confirm to the user that the reminder is set
        speak(f"Reminder set! I’ll remind you to {text} in {minutes} minutes.")
        return True
    except Exception as e:
        # Inform the user if something goes wrong
        speak("Sorry, couldn't set the reminder.")
        return False

# Function to clear all scheduled reminders
def clear_reminders():
    schedule.clear()
    speak("All reminders cancelled.")     
