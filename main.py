# Password Generator Project
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','&','*','/','(',')','+','^']
numbers = ['0','1','2','3','4','5','6','7','8','9']
print("Welcome to the PyPassword Generator!")
no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))
 
password_list = []
for char in range(1 , no_of_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char

for char in range(1 , no_of_symbols + 1):
    random_char = random.choice(symbols)
    password_list += random_char

for char in range(1 , no_of_numbers + 1):
    random_char = random.choice(numbers)
    password_list += random_char

# change the order of list 
random.shuffle(password_list)

# change list into string
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")