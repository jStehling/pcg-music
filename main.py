# This is a sample Python script.
from midiutil import MIDIFile
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from midi_player import MIDIPlayer
from midi_player.stylers import basic, cifka_advanced

from midiutil import MIDIFile

# 4 tracks: piano, bass, flute, drums
midi = MIDIFile(2)

tempo = 600
for track in range(4):
   midi.addTempo(track, 0, tempo)

# --- Track 0: Piano (channel 0) ---
midi.addTrackName(1, 0, "electric guitar")
midi.addProgramChange(1, 0, 0, 93)       # track, channel, time, program (0 = Acoustic Grand Piano)

midi.addNote(1, 0, 50, 1, 4, 100)

"""
# --- Track 2: Flute (channel 2) ---
midi.addTrackName(2, 0, "Flute")
midi.addProgramChange(2, 2, 0, 118)      # synth voice
midi.addNote(2, 2, 76, 0, 2, 80)
midi.addNote(2, 2, 79, 2, 2, 80)

"""

midi.addTrackName(0, 0, "Drums")
midi.addNote(0, 9, 38, 1, 0.5, 100)                 # snare on beat 2
midi.addNote(0, 9, 38, 3, 0.5, 100)                 # snare on beat 4
for beat in range(8):
    midi.addNote(0, 9, 35, beat, 0.5, 100)          # kick
    #midi.addNote(0, 9, 35, beat + 0.5, 0.5, 70)     # closed hi-hat




with open("multi_instrument.mid", "wb") as f:
    midi.writeFile(f)
MIDIPlayer("major-scale.mid",400)
