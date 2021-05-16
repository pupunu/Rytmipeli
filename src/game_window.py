from pyglet import window, media, sprite, text, image
from functools import reduce

BLACK = 0, 0, 0, 255


SCORE_FEEDBACK = {'brutal': 'Brutaali',
                  'hard': 'Vaikea',
                  'normal': 'Normaali',
                  'easy': 'Helppo',
                  'weak': 'Heikko'}


class GameWindow(window.Window):
    '''Luokka, joka huolehtii pelin visuaalisista elementeistä
    '''

    def __init__(self, player_name, notes):
        ''' Luokan konstruktori, joka luo uuden peli-ikkunan.

        Args:
            player_name: pelaajan nimi
            notes: pelissä olevat nuottirivit
        '''

        self.notes = notes

        super(GameWindow, self).__init__(caption='rytmipeli')

        # luodaan tekstikentät
        self.feedback_label = text.Label(
            '', x=510, y=305, anchor_x='center', color=BLACK)
        self.player_name_label = text.Label(
            player_name, x=480, y=150, color=BLACK)
        self.points_label = text.Label('0', x=480, y=120, color=BLACK)

        # luodaan nuottien kuvat
        noteF_img = image.load('data/graphics/sammakko.png')
        noteG_img = image.load('data/graphics/sammakkoG.png')
        noteH_img = image.load('data/graphics/sammakkoH.png')
        noteJ_img = image.load('data/graphics/sammakkoJ.png')
        self.notes_images = noteF_img, noteG_img, noteH_img, noteJ_img

        # luodaan taustakuva
        bkgr_img = image.load('data/graphics/tausta.png')
        self.background = sprite.Sprite(bkgr_img, x=0, y=0)

        # luodaan maalitaulut
        targetF_img = image.load('data/graphics/maaliF.png')
        targetG_img = image.load('data/graphics/maaliG.png')
        targetH_img = image.load('data/graphics/maaliH.png')
        targetJ_img = image.load('data/graphics/maaliJ.png')

        targetF = sprite.Sprite(targetF_img, x=50, y=50)
        targetG = sprite.Sprite(targetG_img, x=150, y=50)
        targetH = sprite.Sprite(targetH_img, x=250, y=50)
        targetJ = sprite.Sprite(targetJ_img, x=350, y=50)

        self.target_circles = targetF, targetG, targetH, targetJ

        for target in self.target_circles:
            target.anchor_y = 25
            target.anchor_x = 25

    def update_feedback(self, score):
        '''Fuktio, joka muuttaa näytöllä näkyvää tekstiä, siitä minkä arvosanan on viime osumaltaan saanut.

        Args:
            score: uusin osuman arvosana
        '''

        self.feedback_label.text = SCORE_FEEDBACK[score]

    def add_note_to_row(self, i):
        '''Nuottien listaan uuden nuotin

        Args:
            i: minkä indeksin jonoon nuotti lisätään
        '''

        x = 50 + i*100
        note = sprite.Sprite(self.notes_images[i], x=x, y=480+self.notes_images[i].height)
        note.anchor_x = 'center'
        note.anchor_y = 'center'
        self.notes[i].append(note)


    def on_draw(self):
        self.clear()
        
        self.background.draw()

        for target in self.target_circles:
            target.draw()

        for note in reduce(lambda a, b: a+b, self.notes, []):
            note.draw()

        self.feedback_label.draw()
        self.player_name_label.draw()
        self.points_label.draw()
