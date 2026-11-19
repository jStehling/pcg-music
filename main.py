# This is a sample Python script.
import random

from midiutil import MIDIFile
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from midi_player import MIDIPlayer
from midi_player.stylers import basic, cifka_advanced

from midiutil import MIDIFile
import makeRythm as mr
# 4 tracks: piano, bass, flute, drums
MF = MIDIFile(1)

TRACK = 0
CHANNEL = 0
TIME = 0
DURATION = 1

VOLUME = 100
TEMPO = 100

Scales = {"C_MAJOR": [60,62,64,65,67,69,71,72],
          "C_MINOR": [60,62,63,65,67,68,70,72],
          "F_MINOR": [65,67,68,70,72,73,75,77],
          "B_MAJOR": [70,73,75,76,78,80,82]
          }

NOTES = [30,32,34]

MF.addTempo(TRACK, TIME, TEMPO)

rythm_list = mr.makeR_rythm(beat=4, max_bars=4)

for bar in rythm_list:
    for note in bar:
        MF.addNote(TRACK, CHANNEL, random.choice(NOTES), TIME, note, VOLUME)
        TIME += note

with open("midiTest.mid", "wb") as f:
    MF.writeFile(f)

