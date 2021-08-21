from mido import MidiFile

mid1 = MidiFile('input.mid')
for i, track in enumerate(mid1.tracks):
    #print('Track {}: {}'.format(i, track.name))
    for i in range(len(track)):
        msgs=track[i]
        if msgs.type == 'note_on':
            print(msgs)