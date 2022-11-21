def choice():
    print("What do you want to do: ")
    print("1) Identify the components of a time object")
    print("2) Calculate age in days")
    print("3) Print the days of the week")
    print("4) Print the months")
    print("0) Stop")
    choice = int(input("Your choice:\n"))
    return choice

def datetime():
    from datetime import datetime 
    inputTime = input("Enter the date and time in the format 'dd.mm.yyyy hh:mm':\n")

    time = datetime.strptime(inputTime, "%d.%m.%Y %H:%M")
    print("You gave year {}".format(time.year))
    print("You gave month {}".format(time.month))
    print("You gave day {}".format(time.day))
    print("You gave hour {}".format(time.hour))
    print("You gave minute {}\n".format(time.minute))

def length():
    from datetime import datetime
    
    birth = input("Enter your birthday as dd.mm.yyyy:\n")
    birth_date = datetime.strptime(birth,'%d.%m.%Y')
    
    day = birth_date.day
    month = birth_date.month
    year = birth_date.year

    time_now = datetime.now()
    month = time_now.strftime("%B")
    x = time_now - birth_date  
    print("On {} {}, {}, you were {} days old.".format(month, time_now.day, time_now.year, x.days))


def week():
    from datetime import datetime , timedelta
    x = datetime(2022,11,7)
    for i in range(7):
        td = timedelta(i)
        y = x + td
        y = y.strftime("%A")
        print(y)
        
def month():
    from datetime import datetime , timedelta
    x = datetime(2022,1,10)
    for i in range(12):
        td = timedelta(days = 30*i)
        y = x + td
        y = y.strftime("%b")
        print(y)
        
def main():
    print("This program uses libraries to deal with time.")
    while True:
        choiceNum = choice()
        if choiceNum == 1:
            datetime()
        elif choiceNum == 2:
            length()
        elif choiceNum == 3:
            week()
        elif choiceNum == 4:
            month()
        elif choiceNum == 0:
            break

main()


