print("Think of a number between 1 and 100! Type OK to continue.")
isok = input().strip().upper()
oktimeout = 0

while isok != "OK" and oktimeout < 5:
    print("Please type OK to continue.")
    isok = input().strip().upper()
    oktimeout += 1

if oktimeout >= 5:
    print("Too many attempts. Please restart the game.")
else:
    low = 1
    high = 100
    guess = (low + high) // 2

    while True:
        print(f"Is your number {guess}? (Type 'greater', 'lower', or 'equal')")
        playerInput = input().strip().lower()

        if playerInput == "greater":
            low = guess + 1
            guess = (low + high) // 2
        elif playerInput == "lower":
            high = guess - 1
            guess = (low + high) // 2
        elif playerInput == "equal":
            print(f"Great! I guessed your number: {guess}")
            break
        else:
            print("Please respond with 'greater', 'lower', or 'equal'.")
