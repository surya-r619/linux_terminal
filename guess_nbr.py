import random
import os
import time

os.system('clear')

def end():
    os.system('clear')
    print("Thank you!!")
    print("Remind me when you get bored!!")

def game():
    print("1. Easy [Infinite number of guessing]")
    print("2. Hard [only 10 Guessing]")
    print("3. Exit")
    choice = int(input())

    if choice == 1:easy()
    elif choice == 2:hard()
    elif choice == 3:end()
    else:
        print("Invalid input!")
        game()

def easy():
    num = random.randint(0,1000)
    print("Guess the number : ")
    user = 0
    user = int(input())
    count = 1
    while True:
        if num == user:break
        elif num < user:
            print("try lesser number : ")
            user = int(input())
        else:
            print("try greater number : ")
            user = int(input())
        count +=1
    os.system('clear')
    print("Finally!!")
    print("You took {} tries to find {}".format(count,num))
    print("\n\nDo you wanna play again?[y/n] : ")
    play = input()
    if play == ("y" or "Y"):
        game()
    else:end()
    
def hard():
    num = random.randint(0,1000)
    print("Guess the number : ")
    count = 10
    user = 0
    n = 1
    user = int(input())
    while count != 0:
        if num == user:break
        elif num < user:
            print("try lesser number : ")
            user = int(input())
        else:
            print("try greater number : ")
            user = int(input())
        count -=1
        n +=1
    if count:
        os.system('clear')
        print("You are very good at guessing\n")
        print("You took {} tries to find {}".format(n,num))
        print("Do you wanna play again?[y/n] : ")
        play = input()
        if play == ("y" or "Y"):
            game()
        else:end()
    else:
        os.system('clear')
        print("Sorry!!")
        print("You ran out of chances\n\n")
        print("Do you wanna try again?[y/n] : ")
        play = input()
        if play == ("y" or "Y"):
            game()
        else:end()

print("Hello World!")
print("Welcome to the game of Guessing a number\n\n")
print("The game begins in few seconds..")
time.sleep(8)
os.system('clear')


print("This game has two modes..")
print("Number Range 0-1000\n")
game()
