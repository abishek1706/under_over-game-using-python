import random

easy=["apple","tiger","train","trade"]
medium=["computer","laptop","mobile","copy"]
hard=["@abishek123","abi@","abihkl234","pawan@12"]

print("wlecome to password guessing game")
level=input("enter difficulty level easy,medium or hard:").lower()
if level=="easy":
    secret=random.choice(easy)
elif level=="medium":
    secret=random.choice(medium)
elif level=="hard":
    secret=random.choice(hard)
else:
    print("invalid choice! defaulting to easy level")
    secret=random.choice(easy)

attempt=0
print("\nguess the secret password:")
while True:
    guess=input("enter your guess:").lower()
    attempt+=1
    if guess==secret:
        print(f"congrulation you guess the correct password in {attempt} attempt")
        break

    hint=""
    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print("Hint:",hint)
print("Game over!")
