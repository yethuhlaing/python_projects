def question():
    print("What temperature conversion do you want to do?")
    print("1) Celsius -> Fahrenheit")
    print("2) Celsius -> Kelvin")
    print("3) Fahrenheit -> Kelvin")
    print("4) Fahrenheit -> Celsius")
    print("5) Kelvin -> Celsius")
    print("6) Kelvin -> Fahrenheit")
    print("0) Stop")
    
def CF(temp):
    value = temp*9/5 + 32
    print("Temperature in degrees Fahrenheit: {}\n".format(value))
def CK(temp):
    value = temp + 273.15
    print("Temperature in degrees Kelvin: {}\n".format(value))
def FK(temp):
    value = (temp-32)*5/9 + 273.15
    print("Temperature in degrees Kelvin: {}\n".format(value))
def FC(temp):
    value = (temp-32)*5/9
    print("Temperature in degrees Celsius: {}\n".format(value))
def KC(temp):
    value = temp - 273.15
    print("Temperature in degrees Celsius: {}\n".format(value))
def KF(temp):
    value = (temp-273.15)*9/5 + 32
    print("Temperature in degrees Fahrenheit: {}\n".format(value))

def main():
    print("Using version 1.0 of the temperature conversion library.")
    while True:
        question()
        choice = int(input("Your choice:\n"))
        temp = int(input("Enter the starting temperature:\n"))
        match choice:
            case 1:
                CF(temp)
            case 2:
                CK(temp)
            case 3:
                FK(temp)
            case 4:
                FC(temp)
            case 5:
                KC(temp)
            case 6:
                KF(temp)
            case 0:
                break

main()
