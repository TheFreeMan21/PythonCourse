def user_choice():
    choice="a"
    acceptable_values = range(0,10)

    while choice.isdigit()==False and choice not in acceptable_values:
        choice = input("Please enter a number (0-4): ")
        if choice.isdigit() == False:
            print("Sorry that's not a digit!")

    return int(choice)
