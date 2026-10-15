import random

while True:
    user_selection = input("Roll the dice? (y/n): ").lower()

    if user_selection == 'y':
        while True:
            try:
                user_input = int(input("How many dice do you want to roll?"))
            except ValueError:
                print("Invalid input! Please enter a valid input.")
                continue
            
            dice_nums_list = []
            if user_input >= 1:
                for i in range(user_input):
                    dice_roll = random.randint(1, 6)
                    dice_nums_list.append(dice_roll)
                print(f"you rolled: {dice_nums_list}")
                break
            else:
                print("Invalid number! Please enter a valid number.")

    elif user_selection == 'n':
        print("Thank you for playing!")
        break

    else:
        print("Invalid input! Please enter 'y' or 'n'.")