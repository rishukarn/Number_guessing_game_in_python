# Number guessing game in Python
import random
print("Hi welcome to the game, This is a number guessing game.\nYou got 10 chances to guess the number. Let's start the game")

number_to_guess=random.randint(1,100)
# print(number_to_guess)
chances=10
guess_count=0

while(chances!=0):
    user_guess=int(input("Guess a number: "))
    if user_guess>number_to_guess:
        print('Your guess number is is Higher')
        chances-=1
        guess_count+=1
    elif user_guess<number_to_guess:
        print('Your guess number is Lower')
        chances-=1
        guess_count+=1
    else:
        break

if chances!=0:
    print(f'The number is {number_to_guess} and you found it right!! in the {guess_count} attempt')
else:
    print(f'Oops sorry, The number is {number_to_guess} better luck next time')
