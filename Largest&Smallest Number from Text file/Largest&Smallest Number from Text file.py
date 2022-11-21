def smallest_num(fileName):
    with open(fileName, "r") as rf:
        smallest_num = int(next(rf))
        for line in rf:
            line = int(line)
            if line < smallest_num:
                smallest_num = line
    return smallest_num
def largest_num(fileName):
    with open(fileName, "r") as rf:
        largest_num = 0
        for line in rf:
            line = int(line)
            if line > largest_num:
                largest_num = line
    return largest_num
def total(fileName):
    with open(fileName, "r") as rf:
        total = 0
        for line in rf:
            line = int(line)
            total += line
    return total
def main():
    file_name = input("Enter the name of the file containing the data:\n")
    saved_file = input("Enter the name of the file to be saved:\n")
    a = smallest_num(file_name)
    b = largest_num(file_name)
    t = total(file_name)
    with open(saved_file, "w") as wf:
        wf.writelines("The smallest number of steps was {} steps.\n".format(a))
        wf.writelines("The largest number of steps was {} steps.\n".format(b))
        wf.writelines("There were {} steps in total.".format(t))
    with open(saved_file, "r") as rf:
        text = rf.read()
        print(text)
main()
