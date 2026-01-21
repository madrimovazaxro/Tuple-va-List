import os
os.system("cls")

list1=['friend', 'family', 'home', 'office', 'son']
list2=['wife', 'husband', 'friend', 'home', 'game', 'office']

for i in list1:
    if i in list2:
        print(i, end = ", ")