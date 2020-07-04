import mido
from mido import Message

ports = mido.get_output_names()
print("ports", ports)

msg = Message('note_on', note=64, velocity=127, time=960)
print(msg)
with mido.open_output(ports[2]) as outport:
#with mido.oppen_output("FLUID Synth")
    outport.send(msg)



msg = Message('note_off', note=64, velocity=127)

with mido.open_output(ports[2]) as outport:
#with mido.open_output('FLUID Synth (3369):Synth input port (3369:0) 129:0')
#with mido.open_output("FLUID Synth")
    outport.send(msg)

