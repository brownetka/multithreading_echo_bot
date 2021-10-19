import socket
import threading

IP = "localhost"
PORT = 2000
ADDR = (IP, PORT)
DISCONNECT_MSG = "!EXIT"


def handle_client(conn, addr):
    print(f"New connection with address: {addr} has been connected.")

    while True:
        msg = conn.recv(2000).decode("utf-8")
        if msg == DISCONNECT_MSG:
            break

        print(f"[{addr}] {msg}")
        conn.send(msg.encode("utf8"))
    conn.close()


def main():
    print("Server is starting!")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADDR)
    server.listen()
    print(f"Server is listening!")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Total number of connections: {threading.activeCount() - 1}")


if __name__ == "__main__":
    main()
