import csv
import datetime as dt
import sys

import pandas as pd

def menu():
    print("You may select one of the following:\n"
          "1) List available cars\n2) Rent a car\n"
          "3) Return a car\n4) Count the money\n0) Exit")

    try:
        choice= int(input('Please choose from the Menu above: \n'))
    except ValueError:
        print('Option not Included in Menu List')
        menu()

    if choice == 1:
        car_list()
        menu()
    elif choice == 2:
        rent_car()
        menu()
    elif choice == 3:
        car_return()
        menu()
    elif choice == 4:
        count_money()
        menu()
    elif choice == 0:
        print('End of program')
        sys.exit()
    else:
        print('Option not Included in Menu List')
        menu()





with open("Vehicles.txt","r",encoding='utf-8') as vehiclesfile:
        Vehicles=csv.reader(vehiclesfile)

with open("transActions.txt","r",encoding='utf-8') as transactionfile:
        Transactions=csv.reader(transactionfile)

with open("rentedVehicles.txt","r",encoding='utf-8') as rentedfile:
        RentVehicles=csv.reader(rentedfile)

with open("Customers.txt","r",encoding='utf-8') as customersfile:
        Customers=csv.reader(customersfile)




#Vehicles = pd.read_csv("Vehicles.txt", sep=",",names = ['plate number','model','daily_rate','properties'])

#Transactions = pd.read_csv("CTransactions.txt", sep=",",names = ['plate_number','birthday','rent_datetime','return_datetime','duration','price'])

#RentVehicles = pd.read_csv("RentedVehicles.txt", sep=",",names = ['plate_number','birthday','rent_datetime'])

#Customers = pd.read_csv("Customers.txt", sep=",",names = ['birthday','f_name','l_name','email'])

with open("Vehicles.txt","r",encoding='utf-8') as vehiclesfile,open("rentedVehicles.txt","r",encoding='utf-8') as rentedfile:
        Vehicles=csv.reader(vehiclesfile)
        RentVehicles=csv.reader(rentedfile)
        rentedcars= []
        avaliable_cars =[]
        for row in RentVehicles:
            rentedcars.append(row)
        for row in Vehicles:
            if row[0] in rentedcars:
                continue
            else:
                avaliable_cars.append(row[0])
                avaliable_cars.append(row[1])
                avaliable_cars.append(row[2])
                avaliable_cars.append(row[3])



def car_list():
    print('The following cars are avaliable: \n')
    
    with open("Vehicles.txt","r",encoding='utf-8') as vehiclesfile:
        Vehicles=csv.reader(vehiclesfile)
        for row in Vehicles:
            if row[0] in rentedcars:
                continue
            else:
                print("* Reg. nr: ",row[0],", Model: ",row[1],", Price per day: ",row[2],'Properties: ',row[3], sep='')


        menu()  # take you back to the menu


def rent_car():

    car_reg = input('Please input the car registration number: \n')
    if str(car_reg) not in avaliable_cars:
            print('Car not available')
            rent_car()
    elif str(car_reg) in rentedcars:
            print('Car already rented')
            rent_car()
    else:
        customer_check(car_reg)
        menu()


#########################################################################################
"""
    while car_reg not in avaliable_cars:
        car_reg = input('Please input the car registration number: \n')
    else:
        while car_reg in rentedcars:
            print('This car has been rented')
            rent_car()
        else:
            customer_check(car_reg)
"""
##################################################################################################


def customer_check(car_reg):
    b_day = input('Enter your birthday in dd/mm/yyyy format: ')

    try:
        day,month,year = [int(x) for x in b_day.split('/')]
        bday = dt.date(year,month,day)
        age = dt.datetime.now().year - bday.year


        if age > 100:
            print('Age limit exceeded')
            sys.exit()
        elif age < 18:
            print('You must be 18 years and above to rent a car')
            sys.exit()
        else:
            with open("Customers.txt","r",encoding='utf-8') as customersfile:
                Customers=csv.reader(customersfile)
                for row in Customers:
                    if b_day == row[0]:
                        print('Customer exist in file')
                        print(f'Hello', row[1], '\n You rented the car {car_reg}')

            
                with open("rentedVehicles.txt",'a',encoding='utf-8') as rentedfile:
                        rentedinfo=f'{car_reg},{b_day},{dt.datetime.now()}\n'
                        rentedfile.write(rentedinfo)
                        avaliable_cars.remove(car_reg)
                        rentedcars.append(car_reg)

                
                fullname = str(input('Your Fulll name, firstname then last name: '))
                fname = fullname.split()[0].capitalize()
                lname = fullname.split()[1].capitalize()

                email = str(input('Your first name: '))
                while var==True:
                            if '.' in email and '@' in email: #check validity of email
                                print("Valid email address.")
                                var=False
                            else:
                                print("Invalid email address.")
                                email=input("Enter your email address:\n")

                with open("Customers.txt","a",encoding='utf-8') as customersfile:
                    customerinfo=f'{b_day},{fname},{lname},{email}\n'
                    customersfile.write(customerinfo)
                    customersfile.close()
    except ValueError:
        print('Incorrect date format')
        customer_check(car_reg)
    
                
    #################################################################################################################
    """
    
    while b_day not in Customers['birthday'].values.tolist():
        print('Birthday not found')
        b_day=input('Enter your birthday in dd/mm/yyyy format: ')
    else:
        while (b_day in Customers['birthday'].values.tolist()) and (bool(dt.datetime.strptime(b_day, '%d/%m/%Y')) == False):
            print('Please use the correct format')
            b_day=input('Enter your birthday in dd/mm/yyyy format: ')
        else:
            day,month,year = [int(x) for x in b_day.split('/')]
            bday = dt.date(year,month,day)
            age = dt.datetime.now().year - bday.year
            while (b_day in Customers['birthday'].values.tolist() and bool(dt.datetime.strptime(b_day, '%d/%m/%Y')) == True) and age <18 or age > 100:
                print('Oops, you must be between 18 and 100 years')
                b_day=input('Enter your birthday in dd/mm/yyyy format: ')
            else:
                pass
    """
    ########################################################################################################################



def car_return():
    return_reg = str(input('Please input the car registration number: '))
    with open("rentedVehicles.txt","r",encoding='utf-8') as rentedfile:
        RentVehicles=csv.reader(rentedfile)
        for row in RentVehicles:
            if return_reg != row[0]:
                print('Registration Number not found')
                car_return(return_reg)
            else:
                print('Request processing')
                car_rate(return_reg)
                return return_reg
                


def car_rate(return_reg):

    with open("rentedVehicles.txt",'r+',encoding='utf-8') as rentedfile:
        RentVehicles=csv.reader(rentedfile)
        
        for row in RentVehicles:
            if return_reg==row[0]:  #finds and defines the rented cars values in rentedfile 
                b_day=row[1]
                initialdate=row[2]

        with open("rentedVehicles.txt",'r+',encoding='utf-8') as Vehiclesfile:
            Vehicles=csv.reader(Vehiclesfile)
            for i in Vehicles:
                if return_reg == i[0]:
                    price = i[2]

        startdate = dt.datetime.strptime(initialdate, '%d/%m/%Y')
        returndate = dt.datetime.strptime(dt.datetime.now(), '%d/%m/%Y')
        duration = (returndate - startdate).days
        total_pay = price * duration


        with open("transAction.txt",'a',encoding='utf-8') as Transactionfile:
            info = f'{return_reg},{b_day},{initialdate},{dt.datetime.now()},{duration},{total_pay}\n'
            Transactionfile.write(info)

        rentedcars.remove(return_reg)
        avaliable_cars.append(return_reg)
    menu()



def count_money():

    with open("transActions.txt",'r',encoding='utf-8') as transactionsfile:
        t_file=csv.reader(transactionsfile)
        revenue=0
        for x in t_file:
            try:
                number=x[5] #iterates through file and adds sum of each transaction to revenue
                revenue+=round(float(number), 2)
            except IndexError:
                print()
        
        print("\nThe total amount of money is ",revenue," euros \n",sep='')
        menu()

menu()
