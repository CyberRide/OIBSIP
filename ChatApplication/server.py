import socket
import threading

def handle_client(client_socket, address, clients):
    try:
        # Get the username from the client
        username = client_socket.recv(1024).decode('utf-8').strip()
        print(f"{username} connected from {address}")

        # Send a welcome message to the client
        welcome_message = f"Welcome {username}! {len(clients) + 1} people online."
        client_socket.sendall(welcome_message.encode('utf-8'))

        # Broadcast the arrival of a new user to all connected clients
        broadcast_to_clients(client_socket, f"{username} joined the chat.", clients)

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            broadcast_message = f"{message}"
            print(broadcast_message)

            broadcast_to_clients(client_socket, broadcast_message, clients)
    except (socket.error, KeyboardInterrupt):
        pass
    finally:
        remove_client(client_socket, clients)
        # Broadcast the departure of a user to all connected clients
        broadcast_to_clients(client_socket, f"{username} left the chat.", clients)

def broadcast_to_clients(sender_socket, message, clients):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode('utf-8'))
            except socket.error:
                remove_client(client, clients)

def remove_client(client_socket, clients):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

def main():
    host = 'localhost'
    port = 5556
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    clients = []

    try:
        while len(clients) < 2:  # Limit the number of clients to 2
            client_socket, address = server_socket.accept()

            # Handle the client in a new thread
            client_handler = threading.Thread(target=handle_client, args=(client_socket, address, clients))
            client_handler.start()
            clients.append(client_socket)

        print("Maximum number of clients reached. No more connections will be accepted.")

    except KeyboardInterrupt:
        pass
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
