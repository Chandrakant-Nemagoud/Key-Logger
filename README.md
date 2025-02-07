# Key Logger (Network-Based)

## Description
This key logger records keystrokes on any system connected within the same network. It is implemented using Python's `pynput` module for capturing keystrokes and the `socket` module for network communication.

## Features
- Logs keystrokes from multiple systems in the same network.
- Uses Python's `pynput` module to monitor keyboard input.
- Transmits recorded keystrokes over a network using sockets.
- Can be run stealthily in the background.

## Requirements
Ensure you have the following Python modules installed:

```bash
pip install pynput
pip install Sockets
```

## How It Works
1. The key logger script runs on a target system, capturing keystrokes.
2. The script sends the recorded keystrokes over the network to a designated server.
3. The server receives and logs the keystrokes for analysis.

## Setup Instructions

1. Create a Python script (`server.py`) to receive logs:
2. Create a Python script (`client.py`) to capture and send keystrokes:


## Disclaimer
This tool is intended for educational purposes only. Unauthorized use of key loggers is illegal and unethical. Ensure you have proper authorization before running this script.


