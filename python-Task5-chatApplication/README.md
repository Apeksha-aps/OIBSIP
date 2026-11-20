# Python Command-Line Chat Application (OIBSIP - Task 5)

A real-time client-server chat application built using Python's `socket` module by **Apeksha Suhas Phapale** as part of the Oasis Infobyte Internship Program.

## Features
- Establishes a local TCP socket connection between a server and a client (`127.0.0.1:5555`)
- Supports bidirectional real-time message exchange via the command line
- Handles graceful disconnection when either user types `exit`

## How to Run
1. Start the server in the first terminal:
   ```bash
   python server.py
   python client.py
