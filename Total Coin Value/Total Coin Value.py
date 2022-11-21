total = 0
while True:
    coin = int(input("Insert 3 - 7 coins (0 stops): "))
    if coin >= 3 and coin <= 7:
        total += coin
    elif coin == 0:
        print("Amount of coins inserted: {}.".format(total))
        print("Thank you for using the program.")
        break
    elif coin < 3 or coin > 7:
        print("Failed to insert coins. Try to insert 3 - 7 coins at a time (0 ends).")

