def file_write(fileName):
    with open(fileName, "w") as wf:
        while True:
            name = input("Enter a name to save to the file (0 to stop):\n")
            if name == "0":
                break
            wf.write(name + "\n" )
            
            
def file_read(fileName):
    print("The following names are stored in the file '{}':".format(fileName))
    with open(fileName, "r") as rf:
        for line in rf:
            print(line, end = "")

def main():
    fileName = input("Enter the file name to be saved:\n")
    file_write(fileName)
    file_read(fileName)

main()
