fileName = input("Enter the name of the file to be read:\n")
with open(fileName,"r", encoding = "UTF-8") as rf:
    with open("Palindromes.txt", "w") as wf:
        for line in rf:
            line = line.strip().lower()
            if line!= "\n":
                if line == line[::-1]:
                    wf.writelines("row '{}' is a palindrome.\n".format(line))
                else:
                    wf.writelines("row '{}' is not a palindrome.\n".format(line))
    with open("Palindromes.txt", "r") as rf:
        print(rf.read())
