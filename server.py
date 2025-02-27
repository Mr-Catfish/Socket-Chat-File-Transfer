import socket
import threading

# Funktion zum Empfangen von Nachrichten
def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Connection to client lost.")
                break

            # Überprüfen, ob es eine Bildübertragung ist
            if data.decode(errors='ignore') == "SEND_IMAGE":
                print("Sending Image...")
                with open('received_image.jpg', 'wb') as img_file:
                    while True:
                        image_data = client_socket.recv(1024)  # Empfange Bilddaten
                        if not image_data or image_data == b'END_OF_IMAGE':
                            break  # Endmarker empfangen
                        img_file.write(image_data)  # Schreibe Bilddaten in Datei
                print("Picture received and saved!")
            
            # Überprüfen auf Exit-Nachricht
            elif data.decode(errors='ignore').lower() == "exit":
                print("Client cloesed the connection.")
                break
            else:
                print(f"Message from Client: {data.decode(errors='ignore')}")

        except Exception as e:
            print(f"ERROR could not receive data: {e}")
            break

# Funktion zum Senden von Nachrichten
def send_messages(client_socket):
    while True:
        message = input("Server: Put ins a message or 'SEND_IMAGE' for sending a Photo): ")
        
        if message.lower() == 'exit':
            client_socket.send("exit".encode())
            break
        elif message == 'SEND_IMAGE':
            client_socket.send(message.encode())
            try:
                with open('image_to_send.jpg', 'rb') as img_file:
                    while True:
                        image_data = img_file.read(1024)
                        if not image_data:
                            break
                        client_socket.send(image_data)  # Sende Bilddaten
                    client_socket.send(b'END_OF_IMAGE')  # Endmarker senden
                    print("Picture receieved succesfully!")
            except FileNotFoundError:
                print("ERROR: The file 'image_to_send.jpg' could not be found.")
                client_socket.send(b'END_OF_IMAGE')  # Sicherstellen, dass der Endmarker gesendet wird
        else:
            client_socket.send(message.encode())  # Normale Textnachricht senden

def start_server():
    PORT = 12392
    IP = "localhost"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    print("Server waiting for Client...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection to {client_address} established")

    # Starte einen Thread für das Empfangen von Nachrichten
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    # Starte einen Thread für das Senden von Nachrichten
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.daemon = True
    send_thread.start()

    try:
        while True:
            pass  # Der Server läuft weiter
    except KeyboardInterrupt:
        print("Server is Closing...")
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()
