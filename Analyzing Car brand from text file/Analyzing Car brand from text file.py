import pandas as pd
rfile = input("Enter the name of the file to read:")
wfile = input("Enter the name of the file to be written:")
try:
    with open(rfile, "r") as rf:
                with open(wfile, "w") as wf:
                        content = rf.readlines()
                        total_car = [i. rstrip('\n') for i in content]
                        car_category = set(total_car)
                        print("{} car brands and {} cars were identified:".format(
                            len(total_car), len(car_category)))
                        
                        car_dict = pd.value_counts(total_car)
                        for i, j in car_dict.items():
                                print("{}: {} cars".format(i,j))

except IOError:
        print("")

