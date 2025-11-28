# Vigenere Cipher

class VigenereCipher:
    def encrypt(self, message, key):
        cipher_text = []
        key = ''.join([c for c in key.upper() if c.isalpha()])
        key_length = len(key)

        for i, char in enumerate(message):
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                key_char = key[(len(cipher_text)) % key_length]
                key_shift = ord(key_char) - 65
                encrypted_char = chr((ord(char.upper()) - 65 + key_shift) % 26 + offset)
        
                if char.islower():
                    encrypted_char = encrypted_char.lower()
                cipher_text.append(encrypted_char)
            else:
                cipher_text.append(char)
        
        return ''.join(cipher_text)
    
    def decrypt(self, message, key):
        plain_text = []
        key = ''.join([c for c in key.upper() if c.isalpha()])
        key_length = len(key)

        for i, char in enumerate(message):
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                key_char = key[(len(plain_text)) % key_length]
                key_shift = ord(key_char) - 65
                decrypted_char = chr((ord(char.upper()) - 65 - key_shift + 26) % 26 + offset)
        
                if char.islower():
                    decrypted_char = decrypted_char.lower()
                plain_text.append(decrypted_char)
            else:
                plain_text.append(char)
        
        return ''.join(plain_text)

if __name__ == "__main__":
    vigenere_cipher = VigenereCipher()
    message = str(input("Enter a message: "))
    key = str(input("Enter a key: "))

    cipher_text = vigenere_cipher.encrypt(message, key)
    print("Encrypted Text: " + cipher_text)

    decrypted_text = vigenere_cipher.decryp
