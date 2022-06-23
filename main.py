import pynput
from pynput.keyboard import Key, Listener

def on_press(key):     # Executes on each key pressed
    print(key)

with Listener(on_press=on_press) as listener:
    listener.join()     # Start the listener