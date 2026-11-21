import random

import MakeMarkov as MK
barlist = []
patterns = [0,1,2,3,4,5,6,7,8]
t_matrix = MK.make_markov(patterns)

def pattern1():
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(0.25)
    barlist.append(0.25)

def pattern2():
    #barlist.append(0.1)
    #barlist.append(0.1)
    #barlist.append(0.1)
    #barlist.append(0.1)
    #barlist.append(0.1)
    #barlist.append(0.1)
    #barlist.append(0.1)
    #barlist.append(0.1)
    #barlist.append(0.1)
    #barlist.append(0.1)
    barlist.append(0.25)
    barlist.append(0.25)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(0.25)

def pattern3():
    barlist.append(0.25)
    barlist.append(0.25)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)

def pattern4():
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(0.25)
    barlist.append(.125)
    barlist.append(.125)

def pattern5():
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(.125)

def pattern6():
    barlist.append(0.5)
    barlist.append(-0.25)
    barlist.append(.125)
    barlist.append(.125)

def pattern7():
    barlist.append(.125)
    barlist.append(.125)
    barlist.append(-.25)
    barlist.append(.25)
    barlist.append(.25)

def pattern8():
    barlist.append(.25)
    barlist.append(.25)
    barlist.append(-.5)

def pattern9():
    barlist.append(-.25)
    barlist.append(0.5)
    barlist.append(.25)

def findBeat(pattern_i, ):

    length = len(patterns)
    choice = random.random() * 100
    if choice < t_matrix[pattern_i][0]:
        return patterns[0]
    for i in range(1,length):
        if choice > t_matrix[pattern_i][i-1] and choice < t_matrix[pattern_i][i]:
            return patterns[i]
    return -100

def make_rythm(time = 4, max_bars = 0):
    choice = random.choice(patterns)

    while time > 0:
        choice = findBeat(choice)
        match choice:
            case 0:
                pattern1()
            case 1:
                pattern2()
            case 2:
                pattern3()
            case 4:
                pattern4()
            case 5:
                pattern5()
            case 6:
                pattern6()
            case 7:
                pattern7()
            case 8:
                pattern8()
            case 9:
                pattern9()
        time -= 1

    return barlist