secret_number = 42
guess = int(input("Please tell me a number between 0 and 100:"))
if guess == secret_number:
    print("You are a hero!")
else:
    print("Damn loser!")