# Import required modules and libraries
from modules.speech import speak, get_voice_input   # Handles speech output and voice input
from modules.weather import get_weather     # Gets weather information
from modules.web import open_site, search_web   # Opens websites and performs Google searches
from modules.knowledge import answer_general_query    # Answers general questions using Wikipedia
from modules.email import send_email   # Sends email using SMTP
from modules.reminder import set_reminder, clear_reminders  # Manages reminders
from datetime import datetime  # For handling date and time
import schedule, time, random    # Scheduling tasks and managing wait
import re    # Regular expressions for parsing numbers

# Main function to start and control the assistant
def main():
    # Greet the user based on current time
    greet_hour = datetime.now().hour
    greeting = "Good morning" if greet_hour < 12 else "Good afternoon" if greet_hour < 18 else "Good evening"
    speak(f"{greeting}! I'm your assistant, ready to help you today. Ask anything or say 'bye' when you're done.")
    speak("So, how can I assist you?")

    idle_counter = 0  # Tracks silence periods
    idle_messages = [
        "Still here if you need me.",
        "Just hanging out... let me know if you'd like anything.",
        "I'm here whenever you need me."
    ]

    # Main loop to listen for user commands
    while True:
        command = get_voice_input()
        if not command:
            idle_counter += 1
            if idle_counter >= 5:
                speak(random.choice(idle_messages))
                idle_counter = 0
            continue
        idle_counter = 0

        # Exit command
        if any(word in command for word in ["bye", "exit", "close"]):
            speak("See you soon! Stay awesome.")
            break

        # Basic conversation handling
        elif any(word in command for word in ["hello", "hi", "hey"]):
            speak("Hello! How can I help you today?")
        elif "how are you" in command:
            speak("I'm doing great, thanks for asking! How about you?")
        elif "thank you" in command or "thanks" in command:
            speak("You're welcome!")
        elif "who are you" in command:
            speak("I'm your personal voice assistant, always here to help.")

        # Functional commands
        elif "weather" in command:
            get_weather(command)
        elif "time" in command or "date" in command:
            now = datetime.now().strftime("%A, %B %d, %I:%M %p")
            speak(now)
        elif "open" in command:
            open_site(command)
        elif "search" in command or "find" in command:
            search_web(command)

        # Reminder feature
        elif any(phrase in command for phrase in ["set reminder", "set a reminder", "remind me", "reminder"]):
            speak("What should I remind you about?")
            reminder_text = get_voice_input()
            if reminder_text:
                speak("In how many minutes?")
                minutes_text = get_voice_input()
                try:
                    match = re.search(r'\d+', minutes_text)
                    if match:
                        minutes = int(match.group())
                        set_reminder(reminder_text, minutes)
                    else:
                        speak("I couldn't understand the number of minutes.")
                    set_reminder(reminder_text, minutes)
                except ValueError:
                    speak("I couldn't understand the number of minutes.")
            else:
                speak("I didn't catch the reminder text.")
        elif "cancel reminder" in command or "clear reminders" in command:
            clear_reminders()

        # Email feature
        elif "write an email" in command or "send email" in command:
            speak("Who should I send the email to?")
            to_address = get_voice_input()
            speak("What's the subject?")
            subject = get_voice_input()
            speak("What's the message?")
            message = get_voice_input()
            if to_address and subject and message:
                success = send_email(to_address, subject, message)
                speak("Email sent successfully." if success else "Failed to send the email.")
            else:
                speak("Missing information; couldn't send the email.")

        # Jokes and general knowledge
        elif "joke" in command:
            speak("Why don’t programmers like nature? Because it has too many bugs!...haha!")
        elif "who is" in command or "what is" in command:
            answer_general_query(command)

        # Fallback handling
        else:
            speak("I'm not sure how to help, but I can search the web if you'd like.")
            confirm = get_voice_input("Shall I look it up?")
            if "yes" in confirm or "sure" in confirm:
                search_web(command)

        # Check scheduled reminders
        schedule.run_pending()
        time.sleep(1)

# Start the assistant
if __name__ == "__main__":
    main()
