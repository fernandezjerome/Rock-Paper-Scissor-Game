from gameComponents import gameVars,gameChar

# define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
    if status == "won":
        pre_message = "Congratulations, you beat the computer. "
        print(gameChar.winner)
    else:
        pre_message = "You done trumped it, loser! "
        print(gameChar.looser)

    print(pre_message + 'Would you like to play again?')

    choice = False

    while choice == False:
        choice = input("Y / N? ")
        if choice.lower().strip() == "y":
            # reset the game loop and start over again
            gameVars.player_lives = gameVars.total_lives
            gameVars.computer_lives = gameVars.total_lives
            gameVars.player_choice = False
        elif choice.lower().strip() == "n":
            # exit message and quita
            print("You chose to quit. Better luck next time!")
            exit()
        else:
            print("Make a valid choice - Y or N")
            choice = False