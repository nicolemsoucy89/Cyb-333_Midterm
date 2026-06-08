import socket

target = input("Enter target (127.0.0.1 or scanme.nmap.org): ")

start_port = int(input("Starting Port: "))
end_port = int(input("Ending Port: "))

if start_port < 1 or end_port > 65535:
    print("Error: Ports must be between 1 and 65535.")
    exit()

for port in range(start_port, end_port + 1):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is closed")

    scanner.close()