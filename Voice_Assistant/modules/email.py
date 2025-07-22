# Import necessary libraries
import smtplib, os, logging   # For sending email, accessing environment variables, and logging errors
from email.message import EmailMessage   # For creating email structure
from dotenv import load_dotenv    # For loading sensitive credentials from a .env file

# Load environment variables from 'id.env' file
load_dotenv("id.env")

# Get the email credentials from the environment file
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Sender's email address
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")   # Sender's email password or app password

# Function to send an email
def send_email(to_address, subject, body):
    try:
        # Create a new email message
        msg = EmailMessage()
        msg['Subject'] = subject        
        msg['From'] = EMAIL_ADDRESS      
        msg['To'] = to_address           
        msg.set_content(body)            

        # Connect securely to Gmail's SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  
            smtp.send_message(msg)                     
        return True   
    except Exception as e:
        # Log any error that occurs while sending the email
        logging.error(f"Email sending error: {e}")
        return False   
