import os
os.system("cls")

N = int(input("N: "))
lst = []
for i in range(N):
    lst.append(input(f"{i+1} -> "))
os.system("cls")

new = []
for i in lst:
    if lst.count(i) >= 2 and i not in new:
        new.append(i)
print(new)