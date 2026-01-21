import os
os.system("cls")

tuple = (2, 3, 4, 5, 1, 8, 7)
juft =0
toq =0
for i in tuple:
    if i%2==0:
        juft += i
    else:
        toq += i
print("Juft: ", juft)
print("Toq: ", toq)