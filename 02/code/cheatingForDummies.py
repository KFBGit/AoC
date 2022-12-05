#! /bin/python3
import sys

class Hand:
    def print(self):
        print(type(self))

class Rock(Hand):
    def fight(opponent):
        if type(opponent) is Sissor:
            return 6
        elif type(opponent) is Rock:
            return 3

class Sissor(Hand):
    def fight(opponent):
        if type(opponent) is Paper:
            return 6
        elif type(opponent) is Sissor:
            return 3

class Paper(Hand):
    def fight(opponent):
        if type(opponent) is Rock:
            return 6
        if type(opponent) is Paper:
            return 3

def decryptHands(input):
    input=input.rstrip()
    match input[0]:
        case 'A':
            opponentsChoice.append(Rock())
        case 'B':
            opponentsChoice.append(Paper())
        case 'C':
            opponentsChoice.append(Sissor())
        case _:
            return None
    match input[1]:
        case 'X':
            guidedChoice.append(Rock())
        case 'Y':
            guidedChoice.append(Paper())
        case 'Z':
            guidedChoice.append(Sissor())
        case _:
            return None

filename=sys.argv[1]
winValues=[]
opponentsChoice=[]
guidedChoice=[]

with open(filename, 'r') as file:
    for line in file:
        decryptHands(line)
