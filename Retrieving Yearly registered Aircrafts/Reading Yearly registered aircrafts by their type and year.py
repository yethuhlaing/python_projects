import csv
import pandas as pd

def main():
    airplane_type = ""
    file = input("Enter filename:")
    line_count(file)
    while True:
        selection = menu()
        match selection:
            case 0:
                airplane_type = "Airplanes"
                analysis(file, airplane_type)
            case 1:
                airplane_type = "Helicopters"
                analysis(file, airplane_type)
            case 2:
                airplane_type = "Ultralights"
                analysis(file, airplane_type)
            case 3:
                airplane_type = "Gliders and Powered Gliders"
                analysis(file, airplane_type)
            case 4:
                airplane_type = "Autogiros"
                analysis(file, airplane_type)
            case 5:
                airplane_type = "Balloons (hot-air)"
                analysis(file, airplane_type)
            case 6:
                airplane_type = "Airships"
                analysis(file, airplane_type)
            case -1:
                break
            case _:
                print("Faulty selection. Please try again.")
    
def menu():
    print("-1) Stop")
    print("0) Airplanes")
    print("1) Calculate Helicopters")
    print("2) Calculate Ultralights")
    print("3) Calculate Gliders and Powered Gliders")
    print("4) Calculate Autogiros")
    print("5) Calculate Balloons (hot-air)")
    print("6) Calculate Airships")
    selection = int(input("Please, make your selection:\n"))
    return selection

def line_count(filename):    
    try:
        with open(filename, "r", encoding='UTF-8') as rf:
            count = len(rf.readlines()) - 1
        print("The file contains {} aircrafts".format(count))
    except IOError:
        print("")


def analysis(fileName, airplane_type):
    try:
        with open(fileName, "r", encoding='UTF-8') as rf:
            contents = csv.reader(rf, delimiter =';')
            header = next(contents)
            
            print("Search type is:{}".format(airplane_type))
            print("Displaying {} in descending order.".format(airplane_type))
            
            group = [i for i in contents if i[2] == airplane_type]            
            year_column = [ i[12] for i in group]
            dict_year = dict(pd.value_counts(year_column))
            dict_year = sorted(dict_year.items(),reverse=True)
            for i, j in dict_year:
                print("{} - {} {}".format(i,j,airplane_type))
            print("Total amount of {} found: {}".format(airplane_type, len(group)))
    except IOError:
        print("Error while processing file {}, exiting.".format(fileName))
    


main()
