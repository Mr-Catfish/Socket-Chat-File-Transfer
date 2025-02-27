# Socket-Chat-File-Transfer
Description: This repository implements a basic chat application with the ability to send and receive text messages and images over a network using Python’s socket and threading libraries.



Files:

    server.py: This script is the server-side of the application. It listens for client connections, handles receiving and sending messages, and supports image transfers. The server accepts client connections, and can send and receive text messages and images. It also allows the server to send an image and receive messages from the client simultaneously.

    user.py: This script is the client-side counterpart. It connects to the server, allows the user to send and receive messages, and supports image sending. Like the server, the client can send text messages and images. It also handles the reception of messages from the server and displays them to the user.

Key Features:

    Real-time Messaging: Both the server and client can send and receive messages in real time.
    Image Transfer: Both sides can send and receive image files. The server sends a static image, while the client can send an image of their choice.
    Multithreading: The server and client each use two threads to handle message sending and receiving concurrently, ensuring non-blocking interactions.
    Graceful Shutdown: Both server and client can handle shutdowns properly, closing the connection when the user inputs "exit".

How it Works:

    Server:
        Starts by listening for a client connection.
        Once connected, it waits for input from the user (server-side).
        Supports sending both text and images.
        Displays any received messages or images.

    Client:
        Connects to the server at the specified IP and port.
        Provides an interface for sending messages and images to the server.
        Displays received messages and images.

Usage:

    Run the Server: Execute server.py to start the server and listen for incoming client connections.
    Run the Client: Execute user.py to start the client and connect to the server.
    Interact: Once connected, you can send text messages or use the special command SEND_IMAGE to send an image (both parties can send/receive images).
    Exit: Type exit to close the connection.

Requirements:

    Python 3.x
    Standard Python libraries (socket, threading)

Notes:

    Ensure the file image_to_send.jpg exists in the same directory as the scripts to send an image.
    The images are saved with a default name (e.g., received_image_from_server.jpg or received_image.jpg).
