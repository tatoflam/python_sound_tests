import mido

file = mido.MidiFile('12GETBA3.MID')

for i, track in enumerate(file.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)

print(file.length)
