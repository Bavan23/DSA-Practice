import random
import time

lowest_num=1
highest_num=100
answers=random.randint(lowest_num,highest_num)
attempts=0

print("\n\n-----------Welcome to Numbeer Guessing Game------------")
time.sleep(1)
print("\nSelect a number between 1 and 100")
time.sleep(1)

while True:
    try:
        guesses=int(input("\nEnter a number between 1,100: "))
        attempts += 1
        if guesses==answers:
            print(f"\nYayyy! You guessed it right in {attempts} guesses!!")
            break
        elif guesses>answers:
            print("\nYour guess is higher than the number I'm thinking of\n")
        else:
            print("\nYour guess is lower than the number I'm thinking of\n")  


    except ValueError:
        print("\nInvalid input")