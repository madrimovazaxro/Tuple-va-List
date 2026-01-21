import os
os.system("cls")

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

for i in range(len(tuple1)):
    print(tuple1[i]+tuple2[i]+tuple3[i], end = " ")