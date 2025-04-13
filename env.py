from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access and print the variables
print("SMTP_SERVER:", os.getenv('SMTP_SERVER'))
print("SMTP_PORT:", os.getenv('SMTP_PORT'))
print("SMTP_USERNAME:", os.getenv('SMTP_USERNAME'))
print("SMTP_PASSWORD:", os.getenv('SMTP_PASSWORD'))
print("RECIPIENT_EMAIL:", os.getenv('RECIPIENT_EMAIL'))