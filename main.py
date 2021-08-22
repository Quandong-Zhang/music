import mido
from mido import MidiFile, MidiTrack,Message

from yin import *


def bpm2tempo(bpm):
    """Convert beats per minute to MIDI file tempo.

    Returns microseconds per beat as an integer::

        240 => 250000
        120 => 500000
        60 => 1000000
    """
    # One minute is 60 million microseconds.
    return int(round((60 * 1000000) / bpm))

mid1 = MidiFile('input.mid')
last_note=-1
tim=0
#
mid = MidiFile(type=1)
track = MidiTrack()
track.append(mido.MetaMessage('set_tempo', tempo=bpm2tempo(75), time=0))
mid.tracks.append(track)
#
for i, track1 in enumerate(mid1.tracks):
    for i in range(len(track1)):
        msgs=track1[i]
        if msgs.type=='note_on' or msgs.type=='note_off':
            tim+=msgs.time
            if msgs.type == 'note_on':
                if msgs.note!=last_note:
                    print('aaaaa')
                    #track.append(Message('note_on',note=msgs.note,channel=0,program= 40,time=msgs.time))
                    track.append(Message('note_on', note=msgs.note ,velocity=64, time=0))
                    #track.append(Message('note_on', note=64, velocity=64,program=40 , time=32))
                    track.append(Message('note_off', note=msgs.note, velocity=64, time=tim))
                    tim=0
                    print("a")
                last_note=msgs.note
                print(last_note)

#mid.tracks.append(track)
mid.save('new_song.mid')