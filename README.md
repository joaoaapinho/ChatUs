<p align="center">
  <img src="static/img/Big_ChatUs_Logo.png?raw=true" alt="Alpine Weather logo" width="35%">
</p>

<h3 align="center">ChatUs - Messaging App</h3>

<p align="center"><b>Done by:</b> João André Pinho</p>


<h2> 👁‍🗨 Overview </h2>

<p> ChatUs is a real-time chat application built using Python and the socket library, that allows users to communicate with each other over a network. The project includes a server and a client application with a graphical user interface using tkinter. 

Take a look at the demo below for a quick overview of the project's flow 🔽</p>
![ChatUs Demo](https://user-images.githubusercontent.com/114337279/235613019-16c2ae57-a24b-4cea-bdeb-e3111b38e5d7.gif)

<h2> 💻 Technology Stack </h2>

Python, Socket library, and Tkinter.

<h2> 🚀 Instructions </h2>

1. **Clone the repository or download the source code.**

```bash
$ git clone https://github.com/joaoaapinho/ChatUs/tree/main
```
2. **Open the chatus_server.py file and modify the hostIP and port variables with the desired server details.**

```
hostIP = "your_host_ip_address_here"
```

3. **Run the server.py file on the desired host in the terminal or by using an IDE.**

```bash
$ python chatus_server.py
```
4. **Run the client.py file on each client device (or multiple if you are testing it on local) in the terminal or by using an IDE.**

```bash
$ python chatus_client.py
```
5. **Enter a username, host IP address, and port number on the login screen of the client application and click "Login."**

6. **Begin sending messages in the chat window, and all connected clients will receive the messages in real-time.**


<h2> 📋 Features </h2>

- Users can connect to the server using a username and an IP address with a port number.
- The server can handle multiple clients simultaneously.
- Broadcast messaging: real-time messages sent by one client are received by all other connected clients.
- Users can type "quit" to gracefully exit the chat application, closing the socket connection and destroying the GUI.

<h2> ⚙️ How it Works </h2>

The ChatUs application consists of two main components: the Server and the Client. 

The server listens for incoming client connections and creates a new thread to manage each client's communication. The client connects to the server using a username, an IP address, and a port number. Once connected, clients can send and receive messages in real-time.

In terms of the breakdown of how these two components work:

<h3> 📡 Server </h3>

1. Create a socket object using the **socket()** function from the socket library with the **IPv4 address** family and the **TCP protocol**.
2. Bind the socket object to a **specific IP address** and **port number** using the **bind()** method. 
3. Listen for incoming client connections using the **listen()** method in a loop.
4. When a new client connection is accepted, **creates a new thread** to manage communication with that client. 
5. The **thread** constinuosly listens for incoming messages from the client using a while loop and broadcasts the message to all other connected clients using the **send()** method on their respective socket objects.

<h3> 📱 Client </h3>

1. Create another **socket** object.
2. Connect to the server using the **connect()** method on the socket object, passing in the server's IP address and port number as arguments.
3. Enter a loop that **listens for incoming messages** from the server using a separate thread, created using the **Thread()** function from the threading library.
4. This function is started in the new thread continuosly listens for incoming messages from the server using a while loop and display them in the client's GUI using the **insert()** method on the Tkinter text widget.
5. Listen to the user input using the **bind()** method on the Entry widget. When the user types a messages and sends it, the message is sent to the server using the **send()** method on the socket object, after appending the client's username to the message.
6. If the user types **"quit"**, the client closes the socket connection using the **close()** methods and destroys the GUI using the **destroy()** method on the Tkinter Tk widget.


<h2> 🎯 Conclusions and Future Improvements </h2>

In summary, the ChatUs - Messaging App is an easy yet effective way for users to communicate in real time over a network. The project is simple to understand and extend, thanks to the usage of the Python socket library and the tkinter GUI toolkit, which enable programmers to change or add new features as necessary. 

While the developed features allow for the core use of any chat app, there are still some improvement opportunities that can be explored in future updates:

- **Private Messaging**: Introducing a feature to send messages to individual users would enhance the usefulness of the app in different scenarios.

- **Encryption**: Implementing end-to-end encryption would greatly enhance the security of the chat application by preventing third party message interceptions.

- **User Authentication**:  Developing a user authentication functionality could help prevent unauthorized access to the chatrooms.

- **File Transfer**: Adding support for file transfer, such as images or documents, would enhance the functionality of the chat application and make it more versatile.
