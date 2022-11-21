def choices():
    print('This calculator can perform the following functions:')
    print('1) Enter the values')
    print('2) Sum')
    print('3) Division')
    print('0) Stop')
    choice = int(input("Select the function (0-3):\n"))
    return choice

def sum(a, b):
    with open("Exercise8_output.txt", "w") as wf:
        total = a + b
        wf.writelines("sum {} + {} = {}\n".format(str(a),str(b),str(total)))
        return total

def division(a , b):
    with open("Exercise6_output.txt", "w") as wf:
        total = a / b
        wf.writelines("sum {} / {} = {}\n".format(a,b,total))
        return total

def main():
    file = input('Enter the name of the file to read:\n')
    choice = choices()
    counter = 0
    while choice != 0:
        if choice == 1:
            with open(file, "r") as rf:
                array = rf.readlines()
                line_num = len(array)
                if counter < line_num:
                    first_num = array[counter].replace('\n', '').strip()
                    second_num = array[counter+1].replace('\n', '').strip()
                    counter += 2  
                    print("Values {} and {} were read".format( first_num, second_num))
                else:
                    print("End of values, end the program.")
                    print("End of values, end the program.")               
                    print("Values 0 and 0 were read")
        elif choice == 2:
            total = sum(int(first_num), int(second_num))
            print("Result saved in file")
            with open("Exercise5_output.txt", "a") as wf:
                wf.writelines("sum {} + {} = {}\n".format(first_num, second_num, total))
        elif choice == 3:
            total = round(division(int(first_num) , int(second_num)),2)
            print("Result saved in file")
            with open("Exercise5_output.txt", "a") as wf:
                wf.writelines("Division {} / {} = {}\n".format(first_num, second_num, total))
        choice = choices()
    print("Stopping")

main()

