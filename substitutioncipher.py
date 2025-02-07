import string
import random

def generate_cipher_alphabet():
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

def encrypt(plaintext, cipher_alphabet):
    plaintext = plaintext.upper()
    ciphertext = "".join(cipher_alphabet.get(char, char) for char in plaintext)
    return ciphertext

def decrypt(ciphertext, cipher_alphabet):
    reverse_cipher = {v: k for k, v in cipher_alphabet.items()}
    plaintext = "".join(reverse_cipher.get(char, char) for char in ciphertext)
    return plaintext

if __name__ == "__main__":
    cipher_alphabet = generate_cipher_alphabet()
    
    message = input("Enter the message to encrypt: ")
    encrypted_msg = encrypt(message, cipher_alphabet)
    decrypted_msg = decrypt(encrypted_msg, cipher_alphabet)
    
    print("Cipher Alphabet:", cipher_alphabet)
    print("Encrypted Message:", encrypted_msg)
    print("Decrypted Message:", decrypted_msg)
