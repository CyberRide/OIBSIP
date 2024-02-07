import socket
import threading

def receive_messages(client_socket, username, should_prompt):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if ': ' in message:
                sender_username, received_message = message.split(': ', 1)
                if sender_username != username:
                    print(f"Received message: {sender_username}: {received_message}")
                else:
                    print(f"Received message: {received_message}")
            else:
                print(f"Received message: {message}")
                
            print("Enter your message:", end=" ", flush=True)  # Prompt for user message
            should_prompt.set()  # Set the flag to prompt for input
    except (socket.error, KeyboardInterrupt):
        pass


def send_messages(client_socket, username, should_prompt):
    try:
        while True:
            if should_prompt.is_set():
                user_message = input()
                full_message = f"{username}: {user_message}"
                client_socket.sendall(full_message.encode('utf-8'))
                should_prompt.clear()  # Clear the flag after sending the message
    except (socket.error, KeyboardInterrupt):
        pass




def main():
    host = 'localhost'
    port = 5556

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the username from the user if not provided
    username = input("Enter your username: ").strip() or "DefaultUser"

    try:
        # Connect to the chat server
        client_socket.connect((host, port))

        # Send the username to the server
        client_socket.sendall(username.encode('utf-8'))

        # Receive and print the welcome message from the server
        welcome_message = client_socket.recv(1024).decode('utf-8')
        print(welcome_message)

        # Create a threading.Event object
        should_prompt = threading.Event()

        # Create two threads for sending and receiving messages
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket, username, should_prompt))
        send_thread = threading.Thread(target=send_messages, args=(client_socket, username, should_prompt))

        # Start the threads
        receive_thread.start()
        send_thread.start()

        # Wait for the threads to finish
        receive_thread.join()
        send_thread.join()

    except socket.error as e:
        print(f"Socket error: {e}")
    except KeyboardInterrupt:
        pass
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
