#Guessing Game:
#Randomly Selects a range
#Then Randomly selects a number in that range

# """for future ideas. Start a point system, Like in those money shows. 
# You'll start with a certain amount of points. 
# Every correct answer gives you a huge point and wrong answers gets some points minus.

import random

print("There will be a range given to you.")
print("You'll have to guess the secret number between that range.")
print("You'll get only 5 guesses.")
print("Are you ready to 'GUESS THAT NUMBER'?")
while 1:
    answer = input("(y)es or (n)o")
    if(answer.lower() == "no" or answer.lower()=="nope" or answer.lower()=="n") :
        break
    #random.state()
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    while not(number1 - number2 > 10 or number1 - number2 < -10):
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)

    if number1 < number2 :
        small = number1
        large = number2
    else:
        small = number2
        large = number1

    secret_number = random.randint(small, large)
    print(f"The secret number is between {small} and {large}")
    guess_limit = 5 #int(input("How many guess do you think you need? "))
    guess_count = 1
    while guess_count <= guess_limit:
        guess = int(input(f"Guess {guess_count}: "))
        if guess == secret_number:
            print("Yay! You won! 🥳🥳🥳😃🥳🥳🥳🥳")
            break
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        guess_count += 1
    else:
        print("😢 You Lost 😢")
        print(f"The secret number was {secret_number}")
    print("Do you still want to play? ")
