from Password_keywords import letters, symbols, numbers
import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for letter in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)

final_pass = ""
for key in password:
    final_pass += key

print(f"Your required password: {final_pass}")
