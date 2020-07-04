import pretty_midi

pm = pretty_midi.PrettyMIDI(resolution=960, initial_tempo=120) 
instrument = pretty_midi.Instrument(0) #instrument is like track

note_number = pretty_midi.note_name_to_number('G4')
note = pretty_midi.Note(velocity=100, pitch=note_number, start=0, end=1) #note on-off

instrument.notes.append(note)
pm.instruments.append(instrument)
pm.write('./midi/test.mid') 
