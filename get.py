import mido
# ['EWI-USB MIDI 1', 'Midi Through Port-0']
with mido.open_input('EWI-USB MIDI 1') as inport:
    for msg in inport:
        print(msg.bytes(), msg.channel, msg.hex(), msg.time, msg.type)
