import random 

number = (random.randrange(1000,10000))
print (number)

attempts = 0
number = str(number)


def guess_number_input():
    while True:
        guess_number = input(("Insert your number (4 digit):"))
        if guess_number.isdigit() and len(guess_number) == 4:
            return guess_number
        else:
            print("Insert 4 digit number!")


def search_number(number, guess_number):
    j = 0
    bulls = 0
    cows = 0
    for i in number:
      if i in guess_number:
            bulls += 1
    for i in guess_number:
        if i == number[j]:
            cows += 1
        j += 1
    print (f"Bulls: {bulls} Cow: {cows}")
    if cows != 4:
        global attempts
        attempts += 1
        search_number(number, guess_number_input())
    return attempts

search_number(number, guess_number_input())

print(f"Great, you have {attempts} attempts")