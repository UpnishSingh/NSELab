import subprocess, os, hashlib

country = input("Country Code (e.g., IN): ")
state = input("State: ")
locality = input("Locality/City: ")
organization = input("Organization Name: ")
org_unit = input("Organizational Unit: ")
common_name = input("Common Name (e.g., localhost): ")
encrypt = input("Encrypt private key? (y/n): ").lower() == "y"

BASE_DIR = "/home/raghu/Documents/NSELab/exp4"
os.makedirs(BASE_DIR, exist_ok=True)

PRIVATE_KEY_FILE = os.path.join(BASE_DIR, "private.key")
CERT_FILE = os.path.join(BASE_DIR, "certificate.crt")

def run_command(cmd):
    res = subprocess.run(cmd, shell=True, text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0: print("Error:", res.stderr)
    return res.stdout

print("Generating private key...")
key_cmd = f"openssl genpkey -algorithm RSA -out \"{PRIVATE_KEY_FILE}\" -pkeyopt rsa_keygen_bits:2048"
if encrypt: key_cmd = key_cmd.replace("genpkey", "genpkey -aes-256-cbc")
run_command(key_cmd)

print("Generating self-signed certificate...")
subject = f"/C={country}/ST={state}/L={locality}/O={organization}/OU={org_unit}/CN={common_name}"
run_command(f"openssl req -new -x509 -key \"{PRIVATE_KEY_FILE}\" -out \"{CERT_FILE}\" -days 365 -subj \"{subject}\"")

# Calculate certificate fingerprint
with open(CERT_FILE, "rb") as f:
    fingerprint = hashlib.sha256(f.read()).hexdigest()

print("Certificate generated successfully.")
print("SHA256 Fingerprint:", fingerprint)
