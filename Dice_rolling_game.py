# dice rooling game
# import random
# number=[1,2,3,4,5,6]
# while True:
#     choice=random.choice(number)

#     print(choice)
#     n=input("do you want to play again?(yes/no)")
#     if n=="no":
#         break

# print("Thank you for playing")

#under and over using dice

# import random

# while True:
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     total = dice1 + dice2

#     n = input("Enter your choice (under/over/draw): ").lower()

#     if n == "under" and total < 6:
#         print("You win 🎉 Total =", total)

#     elif n == "over" and total > 6:
#         print("You win 🎉 Total =", total)

#     elif n == "draw" and total == 6:
#         print("You win 🎉 Total =", total)

#     else:
#         print("You lose 😢 Total =", total)

#     again = input("Do you want to play again? (yes/no): ").lower()
#     if again == "no":
#         break

# print("Thank you for playing 🎲")


#under over betting
import random

balance = 100   # starting money

while balance > 0:
    print("\nYour current balance:", balance)

    bet = int(input("Enter your bet amount: "))
    if bet > balance:
        print("Not enough balance!")
        continue

    choice = input("Enter your choice (under/over/draw): ").lower()

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print("Dice 1:", dice1, "Dice 2:", dice2, "Total:", total)

    if choice == "under" and total < 6:
        print("You WIN 🎉")
        balance += bet

    elif choice == "over" and total > 6:
        print("You WIN 🎉")
        balance += bet

    elif choice == "draw" and total == 6:
        print("You WIN 🎉")
        balance += bet * 2   # higher reward for draw

    else:
        print("You LOSE 😢")
        balance -= bet

    again = input("Play again? (yes/no): ").lower()
    if again == "no":
        break

if balance == 0:
    print("\nGame Over 💀 You lost all your money!")

print("Final balance:", balance)
print("Thank you for playing 🎲")
