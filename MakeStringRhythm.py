import random

import MakeMarkov as MK
patterns = [0,1,2,3,4,5,6,7,8]
t_matrix = MK.make_markov(patterns)

def pattern1(barlist):
    barlist.append(0.5)
    barlist.append(0.25)
    barlist.append(0.25)

def pattern2(barlist):
    barlist.append(0.5)
    barlist.append(0.5)

def pattern3(barlist):
    barlist.append(0.25)
    barlist.append(0.25)
    barlist.append(0.25)
    barlist.append(0.25)

def pattern4(barlist):
    barlist.append(0.25)
    barlist.append(0.25)
    barlist.append(0.5)

def pattern5(barlist):
    barlist.append(1)

def pattern6(barlist):
    barlist.append(0.5)
    barlist.append(-0.25)
    barlist.append(0.25)

def pattern7(barlist):
    barlist.append(-.5)
    barlist.append(.25)
    barlist.append(.25)

def pattern8(barlist):
    barlist.append(.25)
    barlist.append(.25)
    barlist.append(-.5)

def pattern9(barlist):
    barlist.append(-1)

def findBeat(pattern_i, ):

    length = len(patterns)
    choice = random.random() * 100

    if choice < t_matrix[pattern_i][0]:
        return patterns[0]

    for i in range(1,length):
        if choice > t_matrix[pattern_i][i-1] and choice < t_matrix[pattern_i][i]:
            return patterns[i]

    return -100


def make_rythm(time, max_bars = 0):
    choice = random.choice(patterns)
    barlist = []
    while time > 0:
        choice = findBeat(choice)

        match choice:
            case 0:
                pattern1(barlist)
            case 1:
                pattern2(barlist)
            case 2:
                pattern3(barlist)
            case 4:
                pattern4(barlist)
            case 5:
                pattern5(barlist)
            case 6:
                pattern6(barlist)
            case 7:
                pattern7(barlist)
            case 8:
                pattern8(barlist)
            case 9:
                pattern9(barlist)
        time -= 1

    return barlist
