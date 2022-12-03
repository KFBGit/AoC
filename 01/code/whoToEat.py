#! /bin/python3
import sys

filename=sys.argv[1]
counterOfElfs=0
elfCalories=[]
elfCalories.append([])

with open(filename, 'r') as file:
    for line in file:
        if line == '\n':
            counterOfElfs=counterOfElfs + 1
            elfCalories.append([])
            continue
        
        elfCalories[counterOfElfs].append(int(line.rstrip()))

elfCalories.sort(key=sum, reverse=True)
print("The Elf with the most total calories carries: ", sum(elfCalories[0]), "calories")
print("The 3 Elfs who carry the most calories carry a total of: ", (sum(elfCalories[0]) + sum(elfCalories[1]) + sum(elfCalories[2])), "calories")