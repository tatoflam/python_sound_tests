import pretty_midi

midi_data = pretty_midi.PrettyMIDI('./midi/test.mid')
print(midi_data.get_piano_roll())
print(midi_data.synthesize())
