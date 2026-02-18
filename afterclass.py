import random
num = random.randint(1,20)
print("Welcome to the Number Guessing Game!")
user = int(input("The number is between 1 and 20. What's your guess: "))
while user != num:
    user = int(input("Wrong guess! Try again: "))
print("Congratulations! You guessed the number correctly. It was", num)