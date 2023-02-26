import random

number = random.randint(1, 10)
for i in range(0, 3):
    user = int(input("Guess the Number"))
    if user == number:
        print("Bravo!!")
        print(f"You Guessed the Number Right It's {number}")
        break
if user != number:
    print(f"You Made a Wrong Guess, Number is {number}")
