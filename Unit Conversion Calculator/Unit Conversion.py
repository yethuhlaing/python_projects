def main():
    calculation()
def menu():
    print("This is a menu driven program, where you can choose which operation the program performs.")
    print("Choose the operation below:")
    print("1) Grams to pounds")
    print("2) Length conversions")
    print("0) Exit")
    option = int(input("Give option: "))
    return option

def gramsToPounds():
    grams = int(input("Give grams: "))
    pounds = grams * 0.002205
    print("Weight in pounds: {}\n".format(pounds) )

def lengthConversion():
    print("\nSelect units from list: ")
    print("1) Millimeters")
    print("2) Meters")
    print("3) Kilometers\n")
    source = int(input("Source unit(1-3): "))
    target = int(input("Target unit(1-3): "))
    length = float(input("Give length: "))
    return source, target, length
               
def calculation():
    while True:
        option = menu()
        if option == 1:
            gramsToPounds()

        elif option == 2:
            source, target, length = lengthConversion()
            
            if source == 1:
                if target == 2: 
                    converted = length / 1000
                    print("Converted value:", converted , "m\n")
                elif target == 3:
                    converted = length / 1000000
                    print("Converted value:", converted , "km\n")
                elif target == 1:
                    print("There is no conversion because you give the same unit.\n")
                    
            elif source == 2:
                if target == 1:
                    converted = length * 1000
                    print("Converted value:", converted , "mm\n")
                elif target == 3:
                    converted = length / 1000
                    print("Converted value:", converted , "km\n")
                elif target == 2:
                    print("There is no conversion because you give the same unit.\n")
                            
            elif source == 3:
                if target == 1:
                    converted = source * 1000000
                    print("Converted value:", converted , "mm\n")
                elif target == 2:
                    converted = source * 1000
                    print("Converted value:", converted, "m\n")
                elif target == 3:
                    print("There is no conversion because you give the same unit.\n")
        elif option == 0:
            print("Exit")
            break
        else:
            print("Please enter the correct input\n")

    print("Thank you for using the program.")

main()
