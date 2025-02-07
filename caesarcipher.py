import string
import random

def generate_cipher_alphabet():
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

def encrypt_substitution(plaintext, cipher_alphabet):
    plaintext = plaintext.upper()
    ciphertext = "".join(cipher_alphabet.get(char, char) for char in plaintext)
    return ciphertext

def decrypt_substitution(ciphertext, cipher_alphabet):
    reverse_cipher = {v: k for k, v in cipher_alphabet.items()}
    plaintext = "".join(reverse_cipher.get(char, char) for char in ciphertext)
    return plaintext

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    cipher_alphabet = generate_cipher_alphabet()
    
    message = input("Enter the message to encrypt: ")
    encrypted_msg = encrypt_substitution(message, cipher_alphabet)
    decrypted_msg = decrypt_substitution(encrypted_msg, cipher_alphabet)
    
    print("Substitution Cipher Alphabet:", cipher_alphabet)
    print("Encrypted Message (Substitution):", encrypted_msg)
    print("Decrypted Message (Substitution):", decrypted_msg)
    
    shift = int(input("Enter shift value for Caesar Cipher: "))
    caesar_encrypted = caesar_cipher(message, shift, encrypt=True)
    caesar_decrypted = caesar_cipher(caesar_encrypted, shift, encrypt=False)
    
    print("Encrypted Message (Caesar):", caesar_encrypted)
    print("Decrypted Message (Caesar):", caesar_decrypted)