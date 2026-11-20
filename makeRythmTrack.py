import random

def make_rythm(beat=4, max_bars=1):
    rythm_list = []

    #           1/2, 1/4, 1/8

    for bar in range(max_bars):
        bar_list = []
        for i in range(beat):

            bt = 1
            #start of bar
            #add initial beat

            #defining durations and
            #adding durations to bar_list based on bias
            while(bt > 0.17):
                #ensures that a beat always amounts to 1 second
                #if a duration can be subtracted from beat with a positive or 0 difference
                #then allow beat to be available
                durations = []
                if bt - .5 >= 0:
                    durations.append(.5)
                if bt - .25 >= 0:
                    durations.append(.25)
                if bt - .333 >= 0:
                   durations.append(.333)
                #print(bt)
                #print(durations)
                #print("---------")
                dur = random.choice(durations)

                bar_list.append(dur)
                bt -= dur
                #choose next duration based on duration
                #based on initial dur add bias
                #1/4 means next is slightly more likely a 1/4
                #1/2 means next is likely not a 1/2

                #1/8th beats sound too fast(for bass atleast)
                if dur == .333:
                    if random.randint(0,100) > 70:
                        dur = 0.333
                    else:
                        dur = random.choice([.5,.25])
                if dur == .25:
                    if random.randint(0,100) > 65:
                        dur = 0.25
                    else:
                        dur = random.choice([.5,.125])
                if dur == .5:
                    if random.randint(0,100) > 25:
                        dur = .5
                    else:
                        dur = random.choice([.25,.125])

        rythm_list.append(bar_list)
    return rythm_list