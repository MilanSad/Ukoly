import random

number = str(random.randrange(1000,10000))
print (number)
bulls = 0
guess_number = input(("Insert your number (4 digit):"))

for i in number:
    if i in guess_number:
        bulls += 1
print(bulls)