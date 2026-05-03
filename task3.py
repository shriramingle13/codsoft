import random
import string

print("Welcome to the Password Generator!")
print("-----------------------------------")

length = int(input("How long should your password be? "))

use_upper = input("Include uppercase letters? (y/n): ")
use_numbers = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols like !@#$? (y/n): ")

chars = string.ascii_lowercase

if use_upper == 'y':
    chars += string.ascii_uppercase

if use_numbers == 'y':
    chars += string.digits

if use_symbols == 'y':
    chars += string.punctuation

password = ""
for i in range(length):
    password += random.choice(chars)

print("\nYour generated password is:", password)