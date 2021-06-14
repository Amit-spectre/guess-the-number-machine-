import random 
range = int(input("Your number is from 1 to: "))
def computer_guess(x):
    least = 1
    highest = x
    feedback = ''
    while feedback != 'c':
        if least != highest:
            guess = random.randint(least, highest)
        else:
            guess = least
        feedback = input(f"Is {guess} is too high[H] or is too low[l] or correct[C]: ").lower()
        if feedback == 'h':
            highest = guess - 1
        if feedback == 'l':
            least = guess + 1
        
    print ("Yayy! The computer guessed your number correctly")

computer_guess(range)
