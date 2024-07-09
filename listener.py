import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = '172.20.44.137'
port = 5454

# Bind to the port
server_socket.bind((host, port))

# Queue up to 5 requests
server_socket.listen(5)

print(f"Listening on {host}:{port}")

while True:
    # Establish a connection
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")
    
    while True:
        command = input("Enter command: ")
        if command.lower() in ['exit', 'quit']:
            client_socket.close()
            break
        client_socket.send(command.encode())
        response = client_socket.recv(4096).decode()
        print(response)

    if command.lower() in ['exit', 'quit']:
        break

server_socket.close()
