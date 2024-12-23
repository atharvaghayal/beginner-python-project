import hashlib

def crack_hash(hash_to_crack, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            for word in file:
                # Remove any trailing newline characters
                word = word.strip()
                
                # Hash the current word using the same algorithm
                hashed_word = hashlib.sha256(word.encode()).hexdigest()
                
                if hashed_word == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return
        print("[-] Password not found in the wordlist.")
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_file}' not found.")

if __name__ == "__main__":
    # Input: The hash to crack
    hash_to_crack = input("Enter the SHA-256 hash to crack: ").strip()
    # Input: Path to the wordlist file
    wordlist_file = input("Enter the path to your wordlist file: ").strip()
    crack_hash(hash_to_crack, wordlist_file)
