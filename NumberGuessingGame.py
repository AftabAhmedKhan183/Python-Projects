#Number Guessing Game using python
import random

n = int(input("Enter the limit of numbers"))
num = random.randint(1,n)

tries = 0
while True:
    guess = int(input(f"Enter your guess between 1 and {n}:"))

    if num==guess:
        tries += 1
        print(f"Your guess is correct and you took {tries} tries")
        break

    elif num > guess:
        tries += 1
        print("Go a little higher")
    
    elif num < guess:
        tries += 1
        print("Go a little lower")
