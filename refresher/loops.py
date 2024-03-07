number = 7

# while loop
while True:
    user_input = input("Enter 'y' if you would like to play: ").lower()
    
    if user_input == 'n':
        break
            
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("Thats correct!")
    elif abs(number - user_number) == 1:
        print("You're off by one.")
    else:
        print("Sorry, thats wrong")

# for loop
friends = ["adam", "bob", "charlie"]
for friend in friends:
    print(f"My friend {friend} is Canadian")