'''
Python Number Guessing Game 
This is a terminal based game which is played between the user and the computer.  

This is a very interesting game made by importing the random library. 
'''  

import random 

number = random.randint(1,100) 
attempts = 0 

print("🎯 Welcome to the Number Guessing Game") 
print("Guess a number between 1 and 100") 

while True: 
    guess = int(input("enter your guess: ")) 
    attempts += 1 

    if guess < number: 
        print("Too low 📉") 

    elif guess >  number: 
        print("Too high 📈") 

    else: 
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break  

    