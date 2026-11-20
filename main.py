# This is a sample Python script.
import math
import random

from midiutil import MIDIFile
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from midi_player import MIDIPlayer
from midi_player.stylers import basic, cifka_advanced

from midiutil import MIDIFile
from numpy.ma.core import choose

import makeRythmTrack as mr
import matplotlib.pyplot as plt
import numpy as np
# 4 tracks: piano, bass, flute, drums


PITCHES = [60,62,64,65,67,69,71,73]


#takes list of notes and returns a markov chain of transitions
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
            t_matrix[i][j] = random.randint(0,100)
            sums[i] += t_matrix[i][j]

    #
    for i in  range(length):
        for j in range(length):
            t_matrix[i][j] = t_matrix[i][j]/sums[i]

    for row in t_matrix:
        row = np.cumsum(row)

    for i in range(length):
        for j in range(length):
           t_matrix[i][j] = t_matrix[i][j]*100
    for i in range(length):
        row = ""
        for j in range(1,length):
            q = float(t_matrix[i][j])
            row += str(q)
            row += " "

    for i in range(length):
        for j in range(1,length):
            t_matrix[i][j] += t_matrix[i][j-1]

    for i in range(length):
        row = ""
        for j in range(length):
            q = float(t_matrix[i][j])
            row += str(q)
            row += " "
        #print(row)
    return t_matrix


def choose_note(note, t_matrix, notes):
    note_I = findNote(note, notes)
    length = len(notes)
    choice = random.random() * 100
    if choice < t_matrix[note_I][0]:
        return PITCHES[0]

    for i in range(1,length):
        if choice > t_matrix[note_I][i-1] and choice < t_matrix[note_I][i]:
            return PITCHES[i]
    return -1

def findNote(note = -1, scale = [-1]):
    if note == -1 or scale[0] == -1:
        return -1
    for i in range(8):
        if scale[i] == note:
            return i;
    return -1

def make_midi(cycle=1):
    MF = MIDIFile(2)
    RYTHM_TRACK = 0
    STRINGS_TRACK = 1
    CHANNEL = 0

    RYTHM_VOLUME = 100

    #is beats per minute /60 to get beats per bar
    TEMPO = 120
    TIME = 0

    MF.addProgramChange(RYTHM_TRACK, CHANNEL,TIME, 33)#electric bass finger
    MF.addProgramChange(STRINGS_TRACK, CHANNEL, TIME, 91)#electric guitar clean

    MF.addTempo(RYTHM_TRACK, TIME, TEMPO)
    #MF.addTempo(STRINGS_TRACK, TIME, TEMPO)

    rhythm_list = mr.make_rythm(beat=4, max_bars=2)


    for bar in rhythm_list:
        #initial bass pitch for bar
        next_rhythm_note = random.choice(PITCHES)
        rhythm_t_matrix = make_markov(PITCHES)

        next_guitar_note = random.choice(PITCHES)
        guitar_t_matrix = make_markov(PITCHES)

        for step in bar:
            #choose base note
            #next_rhythm_note = choose_note(next_rhythm_note, rhythm_t_matrix, PITCHES)
            #MF.addNote(RYTHM_TRACK, CHANNEL, next_rhythm_note - 32, TIME, step, RYTHM_VOLUME)

            #choose guitar note
            next_guitar_note = choose_note(next_guitar_note, rhythm_t_matrix, PITCHES)
            MF.addNote(STRINGS_TRACK, CHANNEL, next_guitar_note-30, TIME, step, RYTHM_VOLUME)

            TIME += step

    with open("midiTest.mid", "wb") as f:
        MF.writeFile(f)
make_midi()
