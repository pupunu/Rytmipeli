from pyglet import media, window, shapes, clock, text, app
from functools import reduce
from game_logic import check_floor_hit, check_for_hits

WHITE = 255, 255, 255
BLACK = 0, 0, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
YELLOW = 255, 255, 0


def run(song, _):
    win = window.Window(caption = 'rytmipeli')

    colors = BLUE, RED, YELLOW, GREEN
    notes = [], [], [], []

    audio = media.load(song.audiofile)
    feedback_label = text.Label('', x = 400, y = 200, anchor_x = 'center')
    
    colors = BLUE, RED, YELLOW, GREEN
    boxes = []

    for i in range(4):
        box = shapes.Rectangle(x = 50 + i*100, y = 50, width = 50, height = 50, color = colors[i])
        boxes.append(box)
               

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
        if symbol == window.key.F:
            score = check_for_hits(notes[0])
        if symbol == window.key.G:
            score = check_for_hits(notes[1])
        if symbol == window.key.H:
            score = check_for_hits(notes[2])
        if symbol == window.key.J:
            score = check_for_hits(notes[3])
        if score:
            feedback_label.text = score

    def drop_notes(dt):
        for noterow in notes:
            for note in noterow:
                note.y -= 80*dt
                is_hit, message = check_floor_hit(note)
                if is_hit:
                    feedback_label.text = message
                    noterow.remove(note)

    def add_note(_):
        def add_note_to_row(i):            
            color = colors[i]
            x = 50 + i*100
            note = shapes.Rectangle(x = x, y = 400, width = 50, height = 50, color = color)
            notes[i].append(note)    
                
        beat = song.get_next_beat()
        if beat: 
            for i in range(4):
                if beat[i] == '1':
                    add_note_to_row(i)

    if song.offset > 0:
        clock.schedule_once(lambda a: audio.play(), song.offset)
        clock.schedule_interval(add_note, 60.0/song.speed)
    else:
        clock.schedule_once(lambda a: clock.schedule_interval(add_note, 60.0/song.speed), -song.offset)
        audio.play()

    clock.schedule(drop_notes)
    app.run()