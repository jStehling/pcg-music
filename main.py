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

import makeRythm as mr
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
            t_matrix[i][j] = random.randint(0,1000)
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
    for i in range(len(scale)):
        if scale[i] == note:
            return i;
    return -1

def make_midi(cycle=1):
    MF = MIDIFile(4)
    RYTHM_TRACK = 0
    STRINGS_TRACK = 1
    VOICES_TRACK = 2


    RYTHM_VOLUME = 100

    #is beats per minute /60 to get beats per bar
    TEMPO = 120
    TIME = 0
    RHYTHM_TIME = 0
    STRING_TIME = 0
    DRUM_TIME = 0
    #instruments that sound cool: 80, 83, 85, 86,  38, 39,
    MF.addProgramChange(RYTHM_TRACK, 0,TIME, 39)#synth bass 1 = 38 synthbass 2 = 39

    #instruments that sound cool: 84, 83
    MF.addProgramChange(STRINGS_TRACK, 1, TIME, 86)

    #55
    MF.addProgramChange(VOICES_TRACK, 2, TIME, 63)

    MF.addTempo(RYTHM_TRACK, TIME, TEMPO)


    rhythm_list = mr.make_rythm(beat=8, max_bars=2)
    string_list = mr.make_rythm(beat=8, max_bars=2)
    drum_list = mr.make_rythm(beat=8, max_bars=2)

    rhythm_t_matrix = make_markov(PITCHES)
    ooh_t_matrix = make_markov(PITCHES)


    for bar in rhythm_list:
        #initial bass pitch for bar
        next_rhythm_note = random.choice(PITCHES)
        next_ooh_note = random.choice(PITCHES)

        for step in bar:
            #choose base note
            next_rhythm_note = choose_note(next_rhythm_note, rhythm_t_matrix, PITCHES)
            MF.addNote(RYTHM_TRACK, 0, next_rhythm_note-30, TIME, step, 80)

            next_ooh_note = choose_note(next_ooh_note, ooh_t_matrix, PITCHES)
            #MF.addNote(VOICES_TRACK, 2, next_ooh_note, TIME, step, 100)

            TIME += step
    #print(TIME)

    guitar_t_matrix = make_markov(PITCHES)
    for bar in string_list:
        next_guitar_note = random.choice(PITCHES)
        for step in bar:
            next_guitar_note = choose_note(next_guitar_note, guitar_t_matrix, PITCHES)
            MF.addNote(STRINGS_TRACK, 1, next_guitar_note, STRING_TIME, step, 100)
            STRING_TIME += step

    #print(STRING_TIME)
    for bar in drum_list:
        for step in bar:
            #neat drums: 35, 3
            MF.addNote(3, 9, 36, DRUM_TIME, step, 100)
            #if (random.random() * 100 < 10):
                #MF.addNote(3,9,49, DRUM_TIME, .25, 60)
            DRUM_TIME += step
    #print(DRUM_TIME)

    with open("midiTest.mid", "wb") as f:
        MF.writeFile(f)
make_midi()
