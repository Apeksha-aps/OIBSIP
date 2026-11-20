# Project: Chat Application - Client (OIBSIP - Python Programming Task 5)
# Author: Apeksha Suhas Phapale

import socket

HOST = "127.0.0.1"
PORT = 5555

def start_chat_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("\n" + "=" * 46)
    print("      PYTHON CHAT CLIENT - APEKSHA            ")
    print("=" * 46)

    try:
        client_socket.connect((HOST, PORT))
        print(f"Connected to Chat Server at {HOST}:{PORT}")
        print("Type your message below (type 'exit' to quit):\n")

        while True:
            # Send message to server
            client_msg = input("Client (You) : ")
            client_socket.send(client_msg.encode("utf-8"))
            if client_msg.lower() == "exit":
                print("You left the chat.")
                break

            # Receive reply from server
            server_msg = client_socket.recv(1024).decode("utf-8")
            if not server_msg or server_msg.lower() == "exit":
                print("Server ended the chat session.")
                break

            print(f"Server : {server_msg}")

    except ConnectionRefusedError:
        print("Error: Could not connect. Please start 'server.py' first!")
    finally:
        client_socket.close()
        print("Client closed.")

if __name__ == "__main__":
    start_chat_client()
