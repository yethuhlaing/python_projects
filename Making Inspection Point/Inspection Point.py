starting = int(input("Give starting point: "))
stopping = int(input("Give stopping point: "))
inspection = int(input("Give inspection point: "))

if inspection < starting or inspection > stopping:
    print("\nInspection has to be within the range.")
else:
    print("\nFirst loop:")
    for i in range(starting, stopping+1):
        if i == inspection or i == stopping:
            print(i , end = "")
            print("\n")
            break
        print(i , end = " ")
    print("Second loop:")
    for i in range(starting, stopping+1):

        if i == inspection:
            continue
        if i == stopping:
            print(i , end = "")
            print("\n")
            break
        print(i , end = " ")

print("Thank you for using the program.")
        

    
