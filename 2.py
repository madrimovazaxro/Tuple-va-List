import os
os.system("cls")

tuple = (1,2,6,4,2,3,7,9,9,3,10)
for i in range(len(tuple)):
    if i not in tuple and i != 0:
        print(i, end = " ")
