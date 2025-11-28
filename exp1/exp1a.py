# Caesar Cipher

class CaesarCipher:
    def encrypt(self, message, key):
        result = ""

        for char in message:
            if char.isalpha():
                shift = key % 26
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) + (key % 95) - 32) % 95 + 32)
        
        return result
    
    def decrypt(self, message, key):
        result = ""

        for char in message:
            if char.isalpha():
                shift = key % 26
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
            else:
                result += chr((ord(char) - (key % 95) - 32) % 95 + 32)
        
        return result

if __name__ == "__main__":
    caesar_cipher = CaesarCipher()
    message = str(input("Enter a message: "))
    try:
        key = int(input("Enter a key: "))
    except:
        key = 0

    cipher_text = caesar_cipher.encrypt(message, key)
    print("Encrypted Message: ", cipher_text)

    plain_text = caesar_cipher.decrypt(cipher_text, key)
    print("Decrypted Message: ", plain_text)
