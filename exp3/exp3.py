import hashlib, random, time

user_secrets = {"alice": "alice_secret_key", "bob": "bob_secret_key"}
used_nonces, failed_attempts = set(), {"alice":0, "bob":0}

def generate_nonce():
    return str(random.getrandbits(40))  # stronger nonce

def hash_response(nonce, secret, username):
    return hashlib.sha256((nonce + secret + username).encode()).hexdigest()

# ---------------- CLIENT -----------------
username = "bob"
secret = user_secrets[username]

nonce = generate_nonce()
print("Server sends nonce:", nonce)

client_response = hash_response(nonce, secret, username)
print(f"Client ({username}) sends response: {client_response}")

# ---------------- SERVER -----------------
print("Time:", time.ctime())

if failed_attempts[username] >= 3:
    print("Account locked due to multiple failures")
elif nonce in used_nonces:
    print("Replay attack detected")
else:
    expected = hash_response(nonce, user_secrets[username], username)
    if client_response == expected:
        print(f"Authentication Successful for user {username}")
        used_nonces.add(nonce)
    else:
        failed_attempts[username] += 1
        print("Authentication Failed")
