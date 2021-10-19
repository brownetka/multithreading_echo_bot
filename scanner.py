import socket
import tqdm
import threading

new_thread = threading.Thread()

opened_ports = []
N = 100000
for port in tqdm.tqdm(range(1, N + 1)):
    sock = socket.socket()
    try:
        sock.connect(('localhost', port))
        opened_ports.append(port)
    except:
        continue
    finally:
        sock.close()
print("Opened ports:")
for port in opened_ports:
    print(port)
