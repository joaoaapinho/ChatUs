#---------------------------------------------------------------------------------------
# ChatUs Server
#---------------------------------------------------------------------------------------

# Import the necessary Python libraries and modules
from socket import *
from threading import *

# Create an empty set to store all the active client connections
clients = set()

# Function that assigns a thread to each client
def clientThread(clientSocket, clientAddress):
    while True:
        try:
            # Receive an encrypted message from the client and decode it
            message = clientSocket.recv(1024).decode("utf-8")

            # If there is no message (i.e., pressing enter with no message), the client is removed from the set of active connections and a message "disconnected" is printed
            if not message:
                clients.remove(clientSocket)
                print(clientAddress[0] + ": " + str(clientAddress[1]) + " disconnected")
                break

            # Print the message, the client's IP address (clientAddress[0]) and Port number (clientAddress[1])
            print(message)

            # Send the message to every connected client except for the one that sends it (clientSocket)
            for client in clients:
                if client is not clientSocket:
                    # Send the message after encoding it again with the same encoder previously used to decode
                    client.send(message.encode("utf-8"))
        except:
            clients.remove(clientSocket)
            print(clientAddress[0] + ": " + str(clientAddress[1]) + " disconnected")
            break

    # Close the client socket connection
    clientSocket.close()

# Create a socket object with AF_INET (IPv4) and SOCK_STREAM (TCP - Transmission Control) protocols
hostSocket = socket(AF_INET, SOCK_STREAM)

# Configure a SO_REUSEADDR option on the hostSocket so that the address and port number can be reused
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Descriminate the IP address and Port number that the host should be linked
hostIP = "127.0.0.1"
portNumber = 7500
hostSocket.bind((hostIP, portNumber))

# Listen for incoming client connections
hostSocket.listen()

# Print a message to indicate that the Server is waiting for connections
print("Waiting for connections...")

# Accept incoming client connection requests indefinitely
while True:
    # Accept new client connection requests
    clientSocket, clientAddress = hostSocket.accept()

    # Add new clientSockets to the set of active client connections
    clients.add(clientSocket)

    # Print a message announcing that a new connection with a given client was established
    print("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))

    # Start a new thread to manage client communication
    thread = Thread(target=clientThread, args=(clientSocket, clientAddress,))
    thread.start()