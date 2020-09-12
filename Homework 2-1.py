print("Hi")
name = ("what's your name?")



print("Hello,",name)

answer = input("let's play a game")

import random
random_number = random.randint(1,100)
win = False
Turns =0
while win==False:
    Your_guess = input("Think of random number from 1 to 100 and I'll try to guess it")
    Turns +=1
    if random_number==int(Your_guess):
        print("You won!")
        print("Number of turns you have used: ",Turns)
        win == True
        break
    else:
     if random_number>int(Your_guess):
        print("Your Guess was low, Please enter a higher number")
     else:
        print("your guess was high, please enter a lower number")