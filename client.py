import socket

IP = "localhost"
PORT = 2000
ADDR = (IP, PORT)
DISCONNECT_MSG = "!EXIT"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"Client connected to server with address: {IP}:{PORT}")

    while True:
        msg = input("> ")
        client.send(msg.encode("utf8"))
        if msg == DISCONNECT_MSG:
            client.send(f"User with ADDR:{ADDR} has disconnected".encode("utf8"))
            break
        else:
            msg = client.recv(2000).decode("utf8")
            print(f"[SERVER] {msg}")


if __name__ == "__main__":
    main()
