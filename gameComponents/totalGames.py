while True:
    try:
        total_lives = int(input('Race to how many games? '))        
    except ValueError:
        print("You have to input a number ") 
    else:
        break