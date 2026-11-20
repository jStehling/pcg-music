import random

#4 quarter bear
def make_rythm(beat = 4, max_bars = 0):
    rythmlist =[]
    barlist = []
    doubletriplet = False

    for bar in range(max_bars):
        while(beat > 0.1):
            choice = random.randint(0,9)
            if choice <= 2:
                barlist.append(0.5)
                if random.randint(0,10) > 4:
                    barlist.append(0.25)
                    barlist.append(0.25)
                else:
                    barlist.append(0.5)
                beat -= 1

            if choice == 2 or choice == 3:
                barlist.append(0.25)
                barlist.append(0.25)
                if random.randint(0, 10) > 7:
                    barlist.append(0.25)
                    barlist.append(0.25)
                else:
                    barlist.append(0.5)
                beat -= 1;
            if choice == 4 or doubletriplet:
                barlist.append(0.333)
                barlist.append(0.333)
                barlist.append(0.333)
                if random.randint(0,10) == 3 or random.randint(0,10) == 4:
                    doubletriplet = True
                else:
                    doubletriplet = False
                beat -=1
            if choice == 5 or choice == 6:
                barlist.append(1)
                beat -=1
        rythmlist.append(barlist)
        beat = 4
    return rythmlist