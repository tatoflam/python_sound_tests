import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print("avaialble ports: %s" % available_ports)
synth_port = 2

i = 0
for ports in available_ports:
    if ('Synth input' in ports):
        synth_port = i
    i+=1

if available_ports:
    midiout.open_port(synth_port)
    print("opened: %i - %s" % (synth_port, available_ports[synth_port]))

else:
    midiout.open_virtual_port("My virtual output")

with midiout:
    note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
    note_off = [0x80, 60, 0]
    midiout.send_message(note_on)
    time.sleep(0.5)
    midiout.send_message(note_off)
    time.sleep(0.1)

del midiout
