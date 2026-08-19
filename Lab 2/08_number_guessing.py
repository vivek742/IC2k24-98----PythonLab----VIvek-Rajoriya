import random


number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess the number between 1 and 100.")
print("You have 7 attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))

    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100.")
        continue

    attempts = attempts + 1

    if guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print("Correct!")
        print("Number of attempts:", attempts)
        break

else:
    print("You ran out of attempts.")
    print("The correct number was:", number)
