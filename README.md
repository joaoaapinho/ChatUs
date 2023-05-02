<p align="center">
  <img src="static/img/Big_ChatUs_Logo.png?raw=true" alt="Alpine Weather logo" width="35%">
</p>

<h3 align="center">ChatUs - Messaging App</h3>

<p align="center"><b>Done by:</b> João André Pinho</p>


<h2> 👁‍🗨 Overview </h2>

<p> ChatUs is a real-time chat application built using Python and the socket library, that allows users to communicate with each other over a network. The project includes a server and a client application with a graphical user interface using tkinter. 

Take a look at the demo below for a quick overview of the project's flow 🔽</p>

<h2> 💻 Technology Stack </h2>

Python, Socket library, and Tkinter.

<h2> 🚀 Instructions </h2>

1. Clone the repository or download the source code:

```bash
$ git clone https://github.com/joaoaapinho/ChatUs/tree/main
```
2. Open the chatus_server.py file and modify the hostIP and port variables with the desired server details.

`hostIP = "your_host_ip_address_here"`

3. Run the server.py file on the desired host in the terminal or by using an IDE.

```bash
$ python chatus_server.py
```
4. Run the client.py file on each client device (or multiple if you are testing it on local) in the terminal or by using an IDE.

```bash
$ python chatus_client.py
```
5. Enter a username, host IP address, and port number on the login screen of the client application and click "Login."

6. Begin sending messages in the chat window, and all connected clients will receive the messages in real-time.

<h2> 📋 Features </h2>

- Users can connect to the server using a username and an IP address with a port number.
- The server can handle multiple clients simultaneously.
- Broadcast messaging: real-time messages sent by one client are received by all other connected clients.
- Users can type "quit" to gracefully exit the chat application, closing the socket connection and destroying the GUI.


