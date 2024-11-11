import os

set = set()
c = 0
os.system("cls")
while(c != 10):
    print(f"Введите {10 - c} чисел")
    temp = int(input())
    if temp not in set:
        c += 1
        set.add(temp)
    os.system("cls")
    
print(set)