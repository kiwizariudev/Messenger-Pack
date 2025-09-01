import pywhatkit as kit

def send_whatsapp(number, message):
    kit.sendwhatmsg_instantly(number, message)
    print("💬 WhatsApp message sent successfully!")
