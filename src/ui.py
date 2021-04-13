from pygame import *

class UI:

    def __init__(self):
        self.img = None
        init()
        font.init()

    def main_loop(self):

        screen = display.set_mode((640,480))

        running = True
        while running:
            for current_event in event.get():
                if current_event.type == QUIT:
                    running = False
            screen.blit(self.img, (0, 0))
            display.update()


    def set_text(self, text):
        f = font.Font('src/../data/graphics/Poppins-Thin.ttf', 24)
        self.img = f.render(text, True, (255, 255, 255))
