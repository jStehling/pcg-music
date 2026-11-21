import numpy as np
import random

def make_markov(notes):
    sums = []
    length = len(notes)
    t_matrix = np.eye(length, length)
    for i in range(length):
        sums.append(0)

    #t_matrix is a transition matrix
    #represents probability of note on i to note on j
    #initialize notes with random chance
    #add to sum
    for i in  range(length):
        for j in range(length):
            t_matrix[i][j] = random.randint(0,1000)
            sums[i] += t_matrix[i][j]

    #gathers sums of rows
    for i in  range(length):
        for j in range(length):
            t_matrix[i][j] = t_matrix[i][j]/sums[i]

    #takes each row item and reduces it to a number
    #below 1 depending on how much it added to sum


    #multiply by 100 for values between 0-100
    for i in range(length):
        for j in range(length):
           t_matrix[i][j] = t_matrix[i][j]*100
    for i in range(length):
        row = ""
        for j in range(1,length):
            q = float(t_matrix[i][j])
            row += str(q)
            row += " "

    #every number is added up from previous
    #this is done to give a range
    #if a random number is between i,j and i,j-1 then
    #the next choice will be the one corresponding to j
    for i in range(length):
        for j in range(1,length):
            t_matrix[i][j] += t_matrix[i][j-1]

    for i in range(length):
        row = ""
        for j in range(length):
            q = float(t_matrix[i][j])
            row += str(q)
            row += " "
        print(row)

    return t_matrix