import logo
import random

def game():
    print(logo.welcome_logo)
    h = logo.heads
    t = logo.tails
    HeadOrTails = ["h", "t"]
    # guessing
    print("Coin Flipped.....\n")
    flip = random.choice(HeadOrTails)
    guess = input("\nGuess =>\ntype 'h' for heads or 't' for tails: \n")
        
    if guess == flip:
        print("\nYou're correct.....")
        if flip == "h":
            print("\nIt was.... ", h)
        else:
            print("\nIt was.... ", t)
    else:
        print("\nYou're wrong")
        if flip == "h":
            print("\nIt was.... ", h)
        else:
            print("\nIt was.... ", t)
            
    yn = input("Restart? 'y' or 'n': ")
    if yn == "y":
        game()
    else: print("Goodbye")
game()
