import random

def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "C":
        if low > high:
            print("Ops! Seems like we have lost your number..")
        elif low != high:
            guess = random.randint(low, high)
        else:
            guess = low         ##or high, since low=high
        feedback = input(f"Is {guess} lower (L), higher (H) or correct (C)?: ").upper()
        if feedback == "L":
            low = guess + 1
        elif feedback == "H":
            high = guess - 1
        
    print(f"\nCongrats! You guessed the num {guess} correctly. ")

computer_guess(10)