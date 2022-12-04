#! /bin/python3
import sys

filename=sys.argv[1]

with open(filename, 'r') as file:
    for line in file:
        print(line.rstrip)