import numpy  as np
print("This program demonstrates use of numpy-matrix.")
row = int(input("Enter amount of rows:\n"))
column = int(input("Enter amount of columns:\n"))
a = np.zeros((row, column), dtype=int)
print("Zero-matrix of the given rows & columns is:")
print(a)
print("Matrix printed with np-formatting:")
for i in range(row):
        for j in range(column):
                a[i , j] = (i + 1) * (j + 1)
print(a)
x = a.flatten()
print(np.sort(x))
print("Matrix printed with elements separated by semicolons:")
for i in range(len(a)):
        print("", end = "\n")
        for j in range(len(a)):
                print(a[i , j], end = "; ")

print("Shaping the matrix. Please, enter the new dimensions.")


while True:
        row = int(input("Enter amount of new rows:\n"))
        column = int(input("Enter amount of new columns:\n"))
        try:
                z = np.reshape(a, (row, column))
                print("Newly shaped matrix is:")
                print(z)
                print("Largest number in the matrix is: {}".format(np.max(a)))
                print("Smallest number in the matrix is: {}".format(np.min(a)))
                print("Sum of all values in the matrix is: {}".format(np.sum(a)))
                break              
        except Exception as e:
                print(e)
              
list_values=[int(item) for item in input("Enter the list items : ").split()]
new_list = sorted(set(list_values))
print("Unique values are: {}".format(new_list))
        
