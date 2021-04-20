from pyglet import *
from functools import reduce

WHITE = 255, 255, 255
BLACK = 0, 0, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
YELLOW = 255, 255, 0

def main(song):
    win = window.Window(caption = 'rytmipeli')

    audio = media.load(song.audiofile)
    feedback_label = text.Label('', x = 400, y = 200, anchor_x = 'center')
    
    colors = BLUE, RED, YELLOW, GREEN
    boxes = []
    notes = [], [], [], []

    for i in range(4):
        box = shapes.Rectangle(x = 50 + i*100, y = 50, width = 50, height = 50, color = colors[i])
        boxes.append(box)
    
    def add_note(dt):
        def add_note_to_row(i):            
            color = colors[i]
            x = boxes[i].x
            note = shapes.Rectangle(x = x, y = 400, width = 50, height = 50, color = color)
            notes[i].append(note)
        
        beat = song.get_next_beat()
        if beat != False: 
            for i in range(4):
                if beat[i] == '1':
                    add_note_to_row(i)


    def drop_notes(dt):
        for noterow in notes:
            for note in noterow:
                note.y -= 80*dt
                if note.y < -50:
                    noterow.remove(note)
                    feedback_label.text = 'Oot huono'
            


    @win.event
    def on_draw():
        win.clear()
        for box in boxes:
            box.draw()
        for note in reduce(lambda a, b : a+b, notes, []):
            note.draw()
        feedback_label.draw()

    @win.event
    def on_key_press(symbol, modifiers):
        def note_hit(row_num):
            for note in notes[row_num]:
                dist = abs(note.y -50)
                if dist < 50:

                    if dist < 10: #lisää ehtoja eri pisteille
                        feedback_label.text = 'Brutaali'
                    elif dist < 20:
                        feedback_label.text = 'Vaikea'
                    elif dist < 30:
                        feedback_label.text = 'Normaali'
                    elif dist < 40:
                        feedback_label.text = 'Helppo'
                    else:
                        feedback_label.text = 'Heikko'

                    notes[row_num].remove(note)


        if symbol == window.key.F:
            note_hit(0)
        if symbol == window.key.G:
            note_hit(1)
        if symbol == window.key.H:
            note_hit(2)
        if symbol == window.key.J:
            note_hit(3)

    if song.offset > 0:
        clock.schedule_once(lambda a: audio.play(), song.offset)
        clock.schedule_interval(add_note, 60.0/song.speed)
    else:
        clock.schedule_once(lambda a: clock.schedule_interval(add_note, 60.0/song.speed), -song.offset)
        audio.play()


    clock.schedule(drop_notes)
    app.run()