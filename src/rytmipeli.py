from ui import *
from song import *

def main():
    game = Game()
    game.load_songs('./../data/songs')
    game.set_player_name()
    game.choose_song()
    


class Game:
    def __init__(self):
        self.catalog = Catalog()
        self.player_name = None
        self.song_playing = None
    

    def set_player_name(self):
        print('Anna nimesi')
        name = input()
        if name == '':
            self.player_name = 'Vierailija'
        else:
            self.player_name = name
        print('Valitsit nimen', self.player_name, '\n')


    def load_songs(self, filename):
        self.catalog.load_songs(filename)


    def choose_song(self):
        print('Biisit:')
        self.catalog.list_songs()
        while True:
            print('Valitse biisi')
            songname = input()
            if self.catalog.does_song_exist(songname):
                self.song_playing = self.catalog.songlist[songname]
                print('Valitsit biisin:', songname,'\n')
                break
            print('epäkelpo nimi\n')




if __name__ == '__main__':
    main()