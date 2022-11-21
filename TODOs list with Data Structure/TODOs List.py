def menu():
    print("Options:")
    print("1) Insert task")
    print("2) Mark done")
    print("3) Display todos")
    print("4) Create a text file")
    print("0) Exit")
    x = int(input("Your choice: "))
    return x

def main():
    print("Welcome to TODO app!")
    lists = []
    while True:
        choice = menu()
        if choice == 1:
            z = input("Insert task name: ")
            lists.append(z)
            print("", end = "\n")
        elif choice == 2:
            print("Here is list of todos:")
            for index, i  in enumerate(lists):
                print(" - {}. {}".format(index + 1, i))
            mark = int(input("Give task number to mark it done: "))
            print("", end = "\n")
        elif choice == 3:
            print("TODOs:")
            for index, i in enumerate(lists):
                if index == mark-1:
                    print(" - [{}] {}".format("x",i))
                    continue
                print(" - [ ] {}".format(i))
                        
            print("", end = "\n")
        elif choice == 4:
            file = input("Please enter your fileName: ")
            file = file + ".txt"
            try:
                with open(file, mode = "w") as wf:
                    for index , i in enumerate(lists):
                        if index == mark-1:
                            wf.writelines(i +";done\n")
                            continue
                        wf.writelines(i+";undone\n")
            except:
                print("Something wrong with your fileName")
        elif choice == 0:
            print("Exiting.")
            break
        else:
            print("Please choose the correct option!\n")
    print("Thank you for using the program.")


main()

