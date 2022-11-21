import math
import random
def area():
    radius = int(input("Enter the radius of the circle as an integer:\n"))
    area = round(math.pow(radius, 2) * math.pi, 2)
    print("With a radius of {}, the area of the circle is {}.\n".format(radius,area))


def guess():
    print("Guess the integer drawn by the program")
    random.seed(1)
    randomNum = random.randint(0, 1000)
    count = 0
    while True:
        guess = int(input("Enter an integer between 0 and 1000:\n"))
        count += 1
        if guess == randomNum:
            break
        elif guess > randomNum:
            print("The requested number is lower.")
        else:
            print("The requested number is higher.")
    print("Correct! You used {} tries to guess the correct integer..\n".format(count))

def choice():
    print("What do you want to do:")
    print("1) Calculate the area of the circle")
    print("2) Guess the number")
    print("0) Stop")
    choice = int(input("Your choice:\n"))
    return choice

def main():
    print("This program uses libraries to solve tasks.")
    while True:
        choiceNum = choice()
        if choiceNum == 1:
            area()
        elif choiceNum == 2:
            guess()
        elif choiceNum == 0:
            break
main()

    
    
    
