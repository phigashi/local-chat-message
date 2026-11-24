import os
import socket
from faker import Faker

fake = Faker('en_US')
server_address = '/tmp/udp_socket_file'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)
print('server listening...')

def build_reply(message: str) -> str:
    normalized = message.strip().lower()
    if "name" in normalized:
        return f"Generated name: {fake.name()}"
    if "email" in normalized:
        return f"Generated email: {fake.email()}"
    if "address" in normalized:
        return f"Generated address: {fake.address().replace(chr(10), ', ')}"
    return f"{fake.sentence()} (received: {message})"

try:
    while True:
        data, client_address = sock.recvfrom(4096)
        if not data:
            continue

        message = data.decode('utf-8', errors='replace')
        reply = build_reply(message)

        if client_address:
            sock.sendto(reply.encode('utf-8'), client_address)
finally:
    sock.close()
    if os.path.exists(server_address):
        os.unlink(server_address)