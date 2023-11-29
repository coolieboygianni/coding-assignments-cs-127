#Gianni Russell
#November 21, 2023
while True:
    user_input = input("Enter a non-empty string: ")
    if user_input:
        print("You entered:", user_input)
        break
    else:
        print("That was empty. Try again.")