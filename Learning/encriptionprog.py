import random
import string


chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)

#encrypt
plain_text=input("Enter the Word to Encrytpt: ")
cipher_text=""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]

print(f"\nOriginal Text: {plain_text}\nEncrypted Text: {cipher_text}")

#decrypt

cipher_text=input("\nEnter the Word to Decrytpt: ")
plain_text=""

for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]

print(f"\nEncrypted Text: {cipher_text}\nPlain Text: {plain_text}")