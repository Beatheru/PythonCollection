import random
import sys

number = random.randint(1, 20)
count = 0
guess = 0

print("Guess my number")
while guess != number:
    guess = int(input())
    count += 1
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct")
        print("It took you", count, "tries")
        sys.exit()
