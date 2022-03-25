from random import choices, randint
from gameComponents import gameVars, winLose, gameChar


while gameVars.player_choice is False:
    print(gameChar.twoChar)
    print("              Your Lives:", gameVars.player_lives, "/", gameVars.total_lives,"                                                 Computer Lives", gameVars.computer_lives, "/", gameVars.total_lives )
    print("Choose your weapon! Or type quit to exit\n") #\n means "new line"

       
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")
    gameVars.player_choice = gameVars.player_choice.lower() # Convertion all input to lower case to filter more choices

    if gameVars.player_choice == "quit" or gameVars.player_choice == "q":        
        print("You chose to quit")
        exit()
    elif ValueError:
        print("You have to input a number ") 


    gameVars.computer_choice = gameVars.choices[randint(0, 2)]
    print("user chose: " + gameVars.player_choice)
    print("computer chose: " + gameVars.computer_choice)
                
    if gameVars.computer_choice == gameVars.player_choice: # their are 9 combination, by doing == reduce the 3 combinations   
        print("It's a \u001b[33mdraw\u001b[37m!")  # added orange colour for draw       
    elif (gameVars.computer_choice == "rock" and gameVars.player_choice =="scissors") or (gameVars.computer_choice == "paper" and gameVars.player_choice =="rock") or (gameVars.computer_choice == "scissors" and gameVars.player_choice =="paper") : # combine 3 combination when computer win
        gameVars.player_lives -= 1
        print(" you \u001b[31mlose!\u001b[37m. Player lives:", gameVars.player_lives) # added red colour for lost
    else: # the rest 3 combination is computer lost
        print("You \u001b[32mWin\u001b[37m! Computer lost 1 life") #added Green colour for win
        gameVars.computer_lives -= 1

    if gameVars.player_lives == 0:
        winLose.winorlose("lost")
    elif gameVars.computer_lives == 0:
        winLose.winorlose("won")
    else:
        gameVars.player_choice = False