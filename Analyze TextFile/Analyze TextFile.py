def main():
    rf = input("Give filename to read: ")
    wf = input("Give filename to write: ")
    while True:
        choice = menu()
        if choice == 1:
            df = readFile(rf)
            print("Read operation completed.\n")           
        if choice == 2:     
            ls = analyze(df)
            print("Analyze operation completed.\n")
        if choice == 3: 
            writeFile(wf,ls)
            print("Write operation completed.\n")
        if choice == 0: 
            print("Exiting.")
            break
    print("Thank you for using the program.\n")            
    

def menu():
    print("Select one of the operations:")
    print("1) Read file")
    print("2) Analyze")
    print("3) Write file")
    print("0) Exit")
    choice = int(input("Your choice: "))
    return choice

def readFile(file):
    with open(file, mode = "r") as rf:
        file = rf.readlines()
    return file

def analyze(readfile):
    ls = []
    for i in readfile:
        if not i.strip().endswith("e"):
            ls.append(i)
    return ls

def writeFile(filename, content):
    with open(filename, mode = "w") as wf:
        wf.writelines(content)
        
main()

    
