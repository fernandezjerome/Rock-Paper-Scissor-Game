choices = ["rock", "paper", "scissors"]

while True:
    try:
        total_lives = int(input('Race to how many games? '))        
    except ValueError:
        print("You have to input a number ") 
    else:
        break

player_lives = total_lives
computer_lives = total_lives
player_choice = False
