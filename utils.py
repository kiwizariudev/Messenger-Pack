from send_email import send_email
from send_whatsapp import send_whatsapp
from send_discord import send_discord
from send_telegram import send_telegram
from send_sms import send_sms

def menu():
    print("Choose a service to send a message:")
    print("1. Email")
    print("2. WhatsApp")
    print("3. Discord")
    print("4. Telegram")
    print("5. SMS")
    choice = input("Enter choice: ")

    if choice == "1":
        sender = input("Your email: ")
        password = input("Your app password: ")
        receiver = input("Receiver email: ")
        message = input("Message: ")
        send_email(sender, password, receiver, message)
    elif choice == "2":
        number = input("Receiver number (with +countrycode): ")
        message = input("Message: ")
        send_whatsapp(number, message)
    elif choice == "3":
        webhook = input("Discord webhook URL: ")
        message = input("Message: ")
        send_discord(webhook, message)
    elif choice == "4":
        token = input("Telegram bot token: ")
        chat_id = input("Chat ID: ")
        message = input("Message: ")
        send_telegram(token, chat_id, message)
    elif choice == "5":
        sid = input("Twilio SID: ")
        token = input("Twilio Auth Token: ")
        sender = input("Twilio phone: ")
        receiver = input("Receiver phone: ")
        message = input("Message: ")
        send_sms(sid, token, sender, receiver, message)
    else:
        print("Invalid choice.")
