# Local Chat Messenger (UDP / UNIX Domain Socket)

A simple local chat messenger built with Python using `AF_UNIX` and `SOCK_DGRAM`, returning replies generated with `Faker`.

## Setup & Usage

```bash
# 1. Create virtual environment and install faker
python3 -m venv .venv
source .venv/bin/activate
python -m pip install faker

# 2. Start the server (in Terminal 1)
python3 server.py

# 3. Start the client (in Terminal 2)
python3 client.py
