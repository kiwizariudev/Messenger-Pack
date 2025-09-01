import requests

def send_discord(webhook_url, message):
    data = {"content": message}
    requests.post(webhook_url, json=data)
    print("🤖 Message sent to Discord!")
