import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# Function to send an email
def send_email(subject, body, to_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "niranjannijuns@gmail.com"  # Replace with your email
    password = "uanj ljkw onlu xoew"  # Use app-specific password for Gmail accounts with 2FA

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)

        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server.sendmail(from_email, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
    finally:
        server.quit()

# Function to generate a random good morning message
def generate_good_morning():
    messages = [
        "Good morning! 🌞 Start your day with a smile and positive thoughts!",
        "Rise and shine! 🌅 May your day be full of joy and success!",
        "Good morning! Wishing you a day filled with happiness and laughter!",
        "Morning! Let's make today amazing!",
        "Good morning! ☕ A fresh day, a fresh start!"
    ]
    return random.choice(messages)

# Function to generate a random good night message
def generate_good_night():
    messages = [
        "Good night! 🌙 Sleep well and recharge for tomorrow!",
        "Night night! 😴 Rest easy and have sweet dreams!",
        "Good night! 🌜 May you have a peaceful and restful night.",
        "Sleep well! 🌟 Tomorrow is a new day full of opportunities.",
        "Good night! 🛏️ Wishing you restful sleep and happy dreams."
    ]
    return random.choice(messages)

# Function to generate a random wellness check message
def generate_wellness_check():
    messages = [
        "How are you doing today? Take a moment for yourself and breathe. 😊",
        "Just checking in! Hope you’re doing well today and taking care of yourself.",
        "How’s everything going today? Remember to relax and take care of yourself!",
        "Hey, how are you feeling today? Don’t forget to drink some water and take breaks.",
        "I hope you're having a good day! Remember to take care of yourself and stay positive."
    ]
    return random.choice(messages)

# Morning message
def send_random_good_morning():
    message = generate_good_morning()
    send_email("Automated Good Morning Reminder", message, "niranjaniju0789@gmail.com")  # Replace with recipient email

# Good night message
def send_good_night_reminder():
    message = generate_good_night()
    send_email("Automated Good Night Reminder", message, "niranjanniju0789@gmail.com")  # Replace with recipient email

# Wellness check
def send_daily_wellness_check():
    message = generate_wellness_check()
    send_email("Automated Wellness Check", message, "niranjanniju0789@gmail.com")  # Replace with recipient email

# Run the functions
send_random_good_morning()
send_good_night_reminder()
send_daily_wellness_check()
