import hashlib, os, time

sender_file = "/home/raghu/Documents/network-security-lab/exp2/sender.txt"

# Step 1: Generate sender.txt hash + size
try:
    with open(sender_file, "rb") as f:
        sender_data = f.read()
        sender_hash = hashlib.sha256(sender_data).hexdigest()
        sender_size = os.path.getsize(sender_file)
except FileNotFoundError:
    print(f"Sender file '{sender_file}' not found.")
    exit(1)

# Step 2: Get receiver file and compare
receiver_file = input("Enter the receiver file path: ").strip()
try:
    with open(receiver_file, "rb") as f:
        receiver_data = f.read()
        receiver_hash = hashlib.sha256(receiver_data).hexdigest()
        receiver_size = os.path.getsize(receiver_file)

    print(f"Time      : {time.ctime()}")
    print(f"Sender Hash   : '{sender_hash}'")
    print(f"Receiver Hash : '{receiver_hash}'")
    print(f"Sender Size   : {sender_size} bytes")
    print(f"Receiver Size : {receiver_size} bytes")

    if receiver_hash == sender_hash and sender_size == receiver_size:
        print("Integrity OK: Hash and size match.")
        status = "MATCH"
    else:
        print("Integrity FAIL: Hash or size mismatch.")
        status = "MISMATCH"

    # Optional logging
    if input("Save log? (y/n): ").lower() == "y":
        with open("integrity_log.txt", "a") as log:
            log.write(f"{time.ctime()} | {status} | {receiver_file}\n")
        print("Log saved.")

except FileNotFoundError:
    print("Receiver file not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
