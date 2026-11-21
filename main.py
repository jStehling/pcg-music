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
import MakeMarkov as MK
import MakeStringRhythm as msr
import makeRythm as mr
import matplotlib.pyplot as plt
import numpy as np
# 4 tracks: piano, bass, flute, drums


PITCHES = [60,62,64,65,67,69,71,73]


#takes list of notes and returns a markov chain of transitions



def choose_note(note, t_matrix, notes):
    note_I = findNote(note, notes)
    length = len(notes)
    choice = random.random() * 100
    if choice < t_matrix[note_I][0]:
        return PITCHES[0]

    for i in range(1,length):

        if choice > t_matrix[note_I][i-1] and choice < t_matrix[note_I][i]:
            return notes[i]
    return -1

def findNote(note = -1, scale = [-1]):
    if note == -1 or scale[0] == -1:
        return -1
    for i in range(len(scale)):
        if scale[i] == note:
            return i;
    return -1

def make_midi(cycle=1):
    MF = MIDIFile(3)
    RYTHM_TRACK = 1
    STRINGS_TRACK = 2
    DRUMS_TRACK = 0

    RYTHM_VOLUME = 100

    #is beats per minute /60 to get beats per bar
    TEMPO = 120
    TIME = 0
    RHYTHM_TIME = 0
    STRING_TIME = 0
    DRUM_TIME = 0
    #instruments that sound cool: 38, 39,
    possible_bass = [38,39]
    MF.addProgramChange(RYTHM_TRACK, 0,RHYTHM_TIME, 39)#synth bass 1 = 38 synthbass 2 = 39

    #fast rhythm
    possible_fast_leads = [81, 87, 27, 28, 29, 90]
    #slow rhythm
    possible_slow_leads = [93]
    MF.addProgramChange(STRINGS_TRACK, 1, STRING_TIME, 81)

    #55
    #MF.addProgramChange(VOICES_TRACK, 2, TIME, 63)

    MF.addTempo(RYTHM_TRACK, TIME, TEMPO)
    #MF.addTempo(STRINGS_TRACK, 4, 120)

    #60bpm params = 18,1,16
    #start time =
    rhythm_list = msr.make_rythm(time=12)

    string_list = msr.make_rythm(time=12)
    drum_list = msr.make_rythm(time=12)


    rhythm_t_matrix = MK.make_markov(PITCHES)
    string_t_matrix = MK.make_markov(PITCHES)

    next_rhythm_note = random.choice(PITCHES)
    for beat in rhythm_list:
        if beat < 0:
            RHYTHM_TIME -= beat
        else:
            next_rhythm_note = choose_note(next_rhythm_note, rhythm_t_matrix, PITCHES)
            MF.addNote(RYTHM_TRACK, 0, next_rhythm_note - 30, RHYTHM_TIME, beat, 100)
            MF.addNote(RYTHM_TRACK, 0, next_rhythm_note - 40, RHYTHM_TIME, beat, 100)
            RHYTHM_TIME += beat

    next_guitar_note = random.choice(PITCHES)
    for beat in string_list:
        if beat < 0:
            STRING_TIME -= beat
        else:
            next_guitar_note = choose_note(next_guitar_note, string_t_matrix, PITCHES)
            MF.addNote(STRINGS_TRACK, 1, next_guitar_note -25, STRING_TIME, beat, 90)
            MF.addNote(STRINGS_TRACK, 1, next_guitar_note -30, STRING_TIME, beat, 90)
            MF.addNote(STRINGS_TRACK, 1, next_guitar_note -20, STRING_TIME, beat, 90)
            STRING_TIME += beat

    for beat in drum_list:
        if beat < 0:
            DRUM_TIME -= beat

        else:
            MF.addNote(DRUMS_TRACK, 9, 36, DRUM_TIME, beat, 100)
            DRUM_TIME += beat

    with open("midiTest.mid", "wb") as f:
        MF.writeFile(f)

make_midi()
