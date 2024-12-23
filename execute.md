Steps to run this program.
<br>
1.Open IDE(Vscode preffered)
<br>
2. open terminal
<br>
3.run "python --version" OR "python3 --version"
<br>
4.Save the code in a file with a .py extension, e.g., hash_cracker.py.
<br>
5.Create or download a wordlist file containing possible passwords, e.g., wordlist.txt.
<br>
6.Each password should be on a new line..
eg:password1
  password123
  qwerty
  admin
<br>
7.run "cd /path/to/your/script"
<br>
8.run"python hash_cracker.py"
<br>
9.Enter the SHA-256 hash to crack: Input the hash you want to crack.
Enter the path to your wordlist file: Provide the file path to the wordlist, e.g., wordlist.txt.
<br>
10.If the hash matches a password in the wordlist, you'll see:
[+] Password found: <password>
If no match is found, you'll see:
[-] Password not found in the wordlist.
<br><br>
EXAMPLE :
$ python hash_cracker.py
Enter the SHA-256 hash to crack: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd8b04a857dff53bf75
Enter the path to your wordlist file: wordlist.txt
[+] Password found: password123
