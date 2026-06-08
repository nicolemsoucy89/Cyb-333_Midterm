import socket

HOST = "127.0.0.1"
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        print("Connected successfully.")

        while True:
            message = input("Enter message: ")

            if message.lower() == "quit":
                break

            client.sendall(message.encode())

            response = client.recv(1024)

            print(response.decode())

except ConnectionRefusedError:
    print("Error: Server is not running.")