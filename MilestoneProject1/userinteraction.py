game_on = True

game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list")
    print (game_list)

def position_choice():
    choice="a"

    while choice not in ['0','1','2']:
        choice=input("Pick a position to replace(0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry, but you did not choose a valid position (0,1,2)")
    
    return int(choice)

def replacement_choice(game_list,position):
    user_replacement= input("Choose what to put there: ")

    game_list[position]=user_replacement

    return game_list

def gameon_choice():
    choice='a'

    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N ")

        if choice not in ['Y','N']:
            print("Please type Y or N")
    
    if choice == 'Y':
        return True
    else:
        return False

while game_on:
    display_game(game_list)

    position=position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on=gameon_choice()