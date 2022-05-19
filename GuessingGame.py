import random

number = random.randint(1,20)
chances = 0

print("Number guessing game")
print("Guess a number (between 1-9)")


while chances < 7:
    guess = int(input("Enter your Guess: "))
    if(guess == number):
        print("Congratulations You Won Yay")
        break
    elif(guess<number): 
        print("Your guess was too low: Guess a number higher than  ", guess)
    else: 
        print("Your guess was too high: Guess a number lower than ", guess)

    chances+=1

if(not chances < 7):
    print("Try again, the number was ", number)