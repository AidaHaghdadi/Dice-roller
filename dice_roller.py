import random

while True:
    user_selection = input("Roll the dice? (y/n): ").lower()

    if user_selection == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"you rolled: {dice1} , {dice2}")

    elif user_selection == 'n':
        print("Thank you for playing!")
        break

    else:
        print("Invalid input! Please enter 'y' or 'n'.")