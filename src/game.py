from pyglet import media, window, clock, app
from game_logic import check_floor_hit, check_for_hits, give_points
from game_window import GameWindow


def run(song, player_name):
    win = GameWindow(caption='rytmipeli', player_name=player_name)

    # biisin alustus
    song.current_beat = -1
    if song.steps == []:
        song.load_steps()

    audio = media.load(song.audiofile)
    player = media.Player()
    player.queue(audio)
    player.seek(0)

    #nuotit tallennetaan tähän
    notes = [], [], [], []

    points = {'brutal': 0, 'hard': 0, 'normal': 0,
              'easy': 0, 'weak': 0, 'total': 0}

    @win.event
    def on_draw():
        win.clear()
        win.draw_all(notes)

    @win.event
    def on_key_press(symbol, modifiers):
        score = False
        if symbol == window.key.F:
            score = check_for_hits(notes[0])
        if symbol == window.key.G:
            score = check_for_hits(notes[1])
        if symbol == window.key.H:
            score = check_for_hits(notes[2])
        if symbol == window.key.J:
            score = check_for_hits(notes[3])
        if score:
            give_points(points, score)
            win.update_feedback(score)

        win.points_label.text = str(points['total'])

    def drop_notes(dt):
        for noterow in notes:
            for note in noterow:
                note.y -= 80*dt
                is_hit, message = check_floor_hit(note)
                if is_hit:
                    win.feedback_label.text = message
                    noterow.remove(note)

    def add_note(_):
        beat = song.get_next_beat()
        if beat:
            for i in range(4):
                if beat[i] == '1':
                    win.add_note_to_row(notes, i)

    #jotta biisi alkaisi oikeaan aikaa, tässä säädetään offset
    if song.offset > 0:
        clock.schedule_once(lambda a: player.play(), song.offset)
        clock.schedule_interval(add_note, 60.0/song.speed)
    else:
        clock.schedule_once(lambda a: clock.schedule_interval(
            add_note, 60.0/song.speed), -song.offset)
        player.play()

    clock.schedule(drop_notes)
    app.run()

    clock.unschedule(drop_notes)
    clock.unschedule(add_note)

    return points
