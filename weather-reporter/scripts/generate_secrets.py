import os, secrets

token = secrets.token_hex(16)
print(f"SECRET_TOKEN={token}")