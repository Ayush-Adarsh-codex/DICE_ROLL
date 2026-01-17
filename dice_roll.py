import random

print("Welcome to The Dice Roll")
while True:
    choice = input("Press 'ENTER' to roll the dice or 'q' to quit: ").strip().lower()

    if choice == "q":
        print("Thanks for playing")
        break
    elif choice == '':
        number = random.randint(1, 6)
        print(f"your number is {number}")
    else:
        print("invalid input")
print("GAME OVER")