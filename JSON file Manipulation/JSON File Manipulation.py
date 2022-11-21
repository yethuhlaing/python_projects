def choices():
    print("What would you like to do?")
    print("1) Calculate total amount of inhabitants by gender")
    print("2) Calculate inhabitants on a given year")
    print("3) Calculate inhabitants after given year by age cohort")
    print("0) Stop\n")
    choice = int(input("Make your choice\n"))
    return choice
    
def gender(fileName):
    import json
    with open(fileName, "r") as rf:
        df = json.loads(rf.read())
    gender = input("Select your gender (0=male, 1=female):\n")
    count = 0
    end = len(df["data"])
    if gender == "0":
        for i in range(end):
            if df["data"][i]["key"][1] == "0":
                count += int(df["data"][i]["values"][0])
        print("There were a total of {} males in Helsinki between years 1900-1961".format(count))
    elif gender == "1":
        for i in range(end):
            if df["data"][i]["key"][1] == "1":
                count += int(df["data"][i]["values"][0])
        print("There were a total of {} females in Helsinki between years 1900-1961".format(count))

def inhabitants(fileName):
    import json
    with open(fileName, "r") as rf:
        df = json.loads(rf.read())
    year = input("Please enter year for search (1900-1961):\n")
    end = len(df["data"])
    count = 0
    for i in range(end):
        if year == df["data"][i]["key"][0]:
            count += int(df["data"][i]["values"][0])
    print("There were a total of {} inhabitants in Helsinki on year {}".format(count,year))


def inhabitants_ages(fileName):
    import json
    with open(fileName, "r") as rf:
        df = json.loads(rf.read())
    year = int(input("Please enter year for search (1900-1961):\n"))
    age = input("Select age cohort (4=20-24, 5 = 25-29, 6 = 30-34, 7=35-39):")
    end = len(df["data"])
    count = 0
    match age:
        case "4":
            for i in range(end):
                if int(df["data"][i]["key"][0]) >= year and df["data"][i]["key"][2] == age:
                    count += int(df["data"][i]["values"][0])
            print("There were a total of {} inhabitants of ages 25-29 between the years 1950 and 1961.".format(count))      
        case "5":
            for i in range(end):
                if int(df["data"][i]["key"][0]) >= year and df["data"][i]["key"][2] == age:
                    count += int(df["data"][i]["values"][0])
            print("There were a total of {} inhabitants of ages 25-29 between the years 1950 and 1961.".format(count))
        case "6":
            for i in range(end):
                if int(df["data"][i]["key"][0]) >= year and df["data"][i]["key"][2] == age:
                    count += int(df["data"][i]["values"][0])
            print("There were a total of {} inhabitants of ages 30-34 between the years 1950 and 1961.".format(count))

        case "7":
            for i in range(end):
                if int(df["data"][i]["key"][0]) >= year and df["data"][i]["key"][2] == age:
                    count += int(df["data"][i]["values"][0])
            print("There were a total of {} inhabitants of ages 35-39 between the years 1950 and 1961.".format(count))

    
def main():
    print("Welcome to history data analyzer.")
    file = input("Enter the file to open:\n")
    print("File read successfully, ready for analysis.")
    while True:
        choice = choices()
        match choice:
            case 1:
                gender(file)
            case 2:
                inhabitants(file)
            case 3:
                inhabitants_ages(file)
            case 0:
                print("Bye!")
                break
            

main()
