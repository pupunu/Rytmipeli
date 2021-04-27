from pyglet import media, window, shapes, clock, text, app, sprite, image
from functools import reduce
from game_logic import check_floor_hit, check_for_hits, give_points

WHITE = 255, 255, 255
BLACK = 0, 0, 0, 255


SCORE_FEEDBACK = {'brutal': 'Brutaali',
                  'hard': 'Vaikea',
                  'normal': 'Normaali',
                  'easy': 'Helppo',
                  'weak': 'Heikko'}


def run(song, player_name):
    win = window.Window(caption='rytmipeli')

    # biisin alustus
    song.current_beat = -1
    audio = media.load(song.audiofile)
    player = media.Player()
    player.queue(audio)
    player.seek(0)
    if song.steps == []:
        song.load_steps()

    notes = [], [], [], []

    feedback_label = text.Label(
        '', x=510, y=305, anchor_x='center', color=BLACK)
    player_name_label = text.Label(player_name, x=480, y=150, color=BLACK)
    points_label = text.Label('0', x=480, y=120, color=BLACK)

    points = {'brutal': 0, 'hard': 0, 'normal': 0,
              'easy': 0, 'weak': 0, 'total': 0}

    target_circles = []  # maalitaulut alhaalla

    # luodaan taustat ja nuottien kuvat
    noteF_img = image.load('data/graphics/sammakko.png')
    noteG_img = image.load('data/graphics/sammakkoG.png')
    noteH_img = image.load('data/graphics/sammakkoH.png')
    noteJ_img = image.load('data/graphics/sammakkoJ.png')
    notes_images = noteF_img, noteG_img, noteH_img, noteJ_img
    bkgr_img = image.load('data/graphics/tausta.png')
    background = sprite.Sprite(bkgr_img, x=0, y=0)

    # luodaan alhaalla olevat maalitaulut
    targetF_img = image.load('data/graphics/maaliF.png')
    targetG_img = image.load('data/graphics/maaliG.png')
    targetH_img = image.load('data/graphics/maaliH.png')
    targetJ_img = image.load('data/graphics/maaliJ.png')

    targetF = sprite.Sprite(targetF_img, x=50, y=50)
    targetG = sprite.Sprite(targetG_img, x=150, y=50)
    targetH = sprite.Sprite(targetH_img, x=250, y=50)
    targetJ = sprite.Sprite(targetJ_img, x=350, y=50)

    target_circles.append(targetF)
    target_circles.append(targetG)
    target_circles.append(targetH)
    target_circles.append(targetJ)

    for target in target_circles:
        target.anchor_y = 25
        target.anchor_x = 25

    @win.event
    def on_draw():
        win.clear()
        background.draw()

        for target in target_circles:
            target.draw()
        for note in reduce(lambda a, b: a+b, notes, []):
            note.draw()

        feedback_label.draw()
        player_name_label.draw()
        points_label.draw()

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
            feedback_label.text = SCORE_FEEDBACK[score]

        points_label.text = str(points['total'])

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
            x = 50 + i*100
            note = sprite.Sprite(notes_images[i], x=x, y=400)
            note.anchor_x = 'center'
            note.anchor_y = 'center'
            notes[i].append(note)

        beat = song.get_next_beat()
        if beat:
            for i in range(4):
                if beat[i] == '1':
                    add_note_to_row(i)

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
