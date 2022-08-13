import random;

number = random.randint(1,50)

def guess_the_number():
    while number > 0:
        ask = int(input("Guess the number! 1 - 50."))
        if ask == number:
            print("Congrats! You guessed the right number!")
        elif ask > number:
            print("Nope, your number is too high. The number was " + str(number))
        elif ask < number:
             print("Nope, your number is too low. The number was " + str(number))
        break
        
guess_the_number()
    


