number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess the number: "))
    if user_input == number:
        print("Thats correct!")
    elif abs(number - user_number) == 1:
        print("You're off by one.")
    else:
        print("Sorry, thats wrong")