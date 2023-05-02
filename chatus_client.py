#---------------------------------------------------------------------------------------
# ChatUs Client
#---------------------------------------------------------------------------------------

# Import the necessary Python libraries and modules
from socket import *
from threading import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Function to receive messages from the server
def recvMessage():
    while True:
        try:
            # Receive messages from the server
            serverMessage = clientSocket.recv(1024).decode("utf-8")

            # Print the message in the console
            print(serverMessage)

            # Display the messages in the message-feed box
            textMessages.insert(END, "\n" + serverMessage)
        except:
            break

# Function that sends user messages to the server
def sendMessage():
    # Receive the message typed by the user
    clientMessage = textYourMessage.get()

    # Check if the message is "quit"
    if clientMessage.lower() == "quit":
        clientSocket.close()
        window.destroy()
    else:
        # Display the message typed by the user
        textMessages.insert(END, "\n" + "You: " + clientMessage)

        # Send the message to the server
        clientSocket.send((username + ": " + clientMessage).encode("utf-8"))

# Function to create a login window
def login():
    global username, hostIP, portNumber
    username = username_entry.get()
    hostIP = ip_address_entry.get()
    portNumber = int(port_entry.get())
    login_window.destroy()

# Create a login window
login_window = Tk()

# Set the icon for the window
img = ImageTk.PhotoImage(Image.open("static/img/c_logo.png"))
login_window.iconphoto(False, img)

# Set window title
login_window.title("ChatUs - Login")

# Load and place the logo
logo = ImageTk.PhotoImage(Image.open("static/img/ChatUs_Logo.png"))
logo_label = Label(login_window, image=logo)
logo_label.grid(row=0, columnspan=2, pady=(10, 20))  # Add some padding to the bottom

# Render and receive the username, IP address and port inputs
username_label = Label(login_window, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10)

username_entry = Entry(login_window, width=50)
username_entry.grid(row=1, column=1, padx=10, pady=10)

ip_address_label = Label(login_window, text="IP Address:")
ip_address_label.grid(row=2, column=0, padx=10, pady=10)

ip_address_entry = Entry(login_window, width=50)
ip_address_entry.grid(row=2, column=1, padx=10, pady=10)

port_label = Label(login_window, text="Port:")
port_label.grid(row=3, column=0, padx=10, pady=10)

port_entry = Entry(login_window, width=50)
port_entry.grid(row=3, column=1, padx=10, pady=10)

login_button = Button(login_window, text="Login", width=20, command=login)
login_button.grid(row=4, columnspan=2, padx=10, pady=10)

login_window.mainloop()

# Create a socket object that will connect to the Server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Define the IP address and Port number of the desired Server (Change these values to the desired ones, right now it runs on Local)
hostIP = "127.0.0.1"
portNumber = 7500

# Establish the connection with the Server using the clientSocket and Server details
clientSocket.connect((hostIP, portNumber))

# Generate a GUI using the library tkinter
window = Tk()

# Set the icon for the window
img = ImageTk.PhotoImage(Image.open("static/img/c_logo.png"))
window.iconphoto(False, img)

window.title("ChatUs - Connected to: " + hostIP + ":" + str(portNumber))

# Create a message-feed box to display the messages from the server
textMessages = Text(window, width=50)
textMessages.grid(row=0, column=0, padx=10, pady=10)

# Create a textbox for the user to input its message
textYourMessage = Entry(window, width=50)
textYourMessage.grid(row=1, column=0, padx=10, pady=10)

# Create a button to send the users' messages
button = Button(window, text="Send message", width=20, command=sendMessage)
button.grid(row=2, column=0, padx=10, pady=10)

# Assign a thread to continuously receive messages from the server
recvThread = Thread(target=recvMessage)

# Set the thread as a daemon, meaning as a background thread that continuously listens for messages from the server
# and prevents the program from exiting when a user closes the window
recvThread.daemon = True
recvThread.start()

# Start tkinter mainloop to display the GUI
window.mainloop()