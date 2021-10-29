import random
import os
import time


os.system('clear')
items = ['Rock', 'Paper', 'Scissor']

#game  defination

def rps():
    points_me = 0
    points_pc = 0
    print("\n\nLoading...")
    time.sleep(3)
    os.system('clear')
    os.system('toilet  --metal -f future.tlf ROCK PAPER SCISSOR')
    
    #Game begins
    print("Let the game begin\n\n")
    time.sleep(3)
    os.system('clear')

    #for looping of the game
    for i in range(1, 10):
        os.system('toilet  --metal -f future.tlf ROCK PAPER SCISSOR')
        print("Round ",i,'\n')
        print("Choose your item/object")
        print("1.Rock\t2.Paper\t3.Scissor")
        choice1 = input()
        choice101 = str.capitalize(choice1)

        #system choice
        num = random.randint(0, 2)
        choice2 = items[num]
        print("\nYour choice is = ",choice101)
        print("Computer choice is = ",choice2)

        #if statments to check choices
        if  choice101 == 'Rock' and choice2 == 'Paper':
            print("Oh no! You lost, Better luck next time\n")
            points_pc += 1
        elif choice101 == "Rock" and choice2 == 'Scissor':
            print("Hey! you won Dude, Keep it going\n")
            points_me += 1
        elif choice101 == "Paper" and choice2 == 'Rock':
            print("Hey! you won Dude, Keep it going\n")
            points_me += 1
        elif choice101 == "Paper" and choice2 == 'Scissor':
            print("Oh no! You lost, Better luck next time\n")
            points_pc += 1
        elif choice101 == "Scissor" and choice2 == 'Rock':
            print("Oh no! You lost, Better luck next time\n")
            points_pc += 1
        elif choice101 == "Scissor" and choice2 == 'Paper':
            print("Hey! you won Dude, Keep it going\n")
            points_me += 1
        elif choice101 == choice2:
            print("Same to Same, Draw!\n")
        else:
            print("Incorrect response")
            time.sleep(5)
            print("Are you so dumb? you can't even spell these simple words")
            time.sleep(5)
            print("Then how the hell are you using LINUX TERMINAL")
            time.sleep(5)
            print("First learn English!!!!! Looser")
            time.sleep(5)
            print("Game crashed")
            print("Loading... Please wait!")
            time.sleep(5)
            os.system('clear')
            exit()

        
        print("Loading next round")
        time.sleep(5)


        os.system('clear')


            #points comaprision for  winning and losing

    os.system('toilet  --metal -f future.tlf ROCK PAPER SCISSOR')
    print('Your points = ',points_me)
    print('Computer points = ',points_pc)

    if points_me > points_pc:
        print("Hurray! you won the Match")
        print("Please wait! Our host is on his way to congradulate you")
        time.sleep(5)
        os.system('xcowsay "Congradulations Dude that was a very good Match"')
        os.system('xcowsay "Thank you for playing this Awesome game"')

    elif points_me == points_pc:
        print("The game has been Draw")
        time.sleep(5)
        os.system('xcowsay "Thanks for playing"')
        
    else:
        print("Oops! You lost this match")
        time.sleep(5)
        os.system('xcowsay "Better luck next time DUDE"')

    #loop back to defination
    print("Do you want to play again? [Y/N]")
    yn1 = input()

    if (yn1 == 'Y' or yn1 == 'y'):
        rps()
    else:
        print("Run the game in your free time")
        print("Loading...")
        time.sleep(2)
        exit()


#Introduction  to program and game

print("Hello World!")
time.sleep(1)
print("Welcome to the simple game\n'ROCK PAPER SCISSOR'")
print("Are you ready to play with Computer? [Y/N]")
yn = input()

if (yn == 'Y' or yn == 'y'):
    print("There will 10 rounds and who has highest points wins the Game\n")
    time.sleep(5)
    rps()
else:
    print("Run the game in your free time")
    print("Loading...")
    time.sleep(5)
    exit()
