import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'
client_address =  '/tmp/udp_client_socket_file'

try:
    os.unlink(client_address)
except FileNotFoundError:
    pass

sock.bind(client_address)

try:
    while True:
        user_input = input()

        if user_input == "exit":
            break
        if not user_input:
            continue

        sock.sendto(user_input.encode("utf-8"), server_address)
        data, _ = sock.recvfrom(4096)
        print('Server reply: ', data.decode("utf-8"))
finally:
    sock.close()
    if os.path.exists(client_address):
        os.unlink(client_address)