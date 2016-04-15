import mido
import turtle

device = 'USB Oxygen 8 v2 MIDI 1'
# device = 'EWI-USB MIDI 1'
note_color = {"C": "#BCE039", "C#": "#149033", "D": "#1B9081", "D#": "#1C0D82",
              "E": "#7F087C", "F": "#D71386", "F#": "#6F0D45", "G": "#A00C09",
              "G#": "#FA0B0C", "A": "#F88010", "A#": "#EDF087", "B": "#F5F43C"}
notes = {
    "C": [number for number in range(0, 121, 12)],
    "C#": [number for number in range(1, 122, 12)],
    "D": [number for number in range(2, 123, 12)],
    "D#": [number for number in range(3, 124, 12)],
    "E": [number for number in range(4, 125, 12)],
    "F": [number for number in range(5, 126, 12)],
    "F#": [number for number in range(6, 127, 12)],
    "G": [number for number in range(7, 128, 12)],
    "G#": [number for number in range(8, 117, 12)],
    "A": [number for number in range(9, 118, 12)],
    "A#": [number for number in range(10, 119, 12)],
    "B": [number for number in range(11, 120, 12)]}


def make_color(note, octave=0):
    print(note)
    note_name = [key for key in notes.keys() if note in notes[key]]
    print(note_name)
    color = note_color[note_name[0]]
    return(color)


with mido.open_input(device) as inport:
    turtle.color('blue', 'green')
    turtle.speed(0)
    turtle.up()
    turtle.setx(-100)
    turtle.down()
    turtle.begin_fill()
    for msg in inport:
        midi_bytes = msg.bytes()
        if(midi_bytes[0] == 144):
            note = midi_bytes[1]
            turtle.bgcolor(make_color(note))
            print("Note: ", note)

        elif(midi_bytes[0] == 176):
            print("Air Pressure: ", midi_bytes[2])
        turtle.forward(200)
        turtle.left(170)
        # print(midi_bytes, "|", msg.channel,  "|",  msg.time, "|",  msg.type)
    turtle.done()
