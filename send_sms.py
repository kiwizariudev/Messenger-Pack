from twilio.rest import Client

def send_sms(account_sid, auth_token, sender, receiver, message):
    client = Client(account_sid, auth_token)
    sms = client.messages.create(body=message, from_=sender, to=receiver)
    print(" SMS sent with Twilio, SID:", sms.sid)
