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