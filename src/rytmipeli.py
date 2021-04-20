from song import load_songs
import game
from ui import *

def main():
    songlist = load_songs(directorypath = 'data/songs/')
    playername = get_player_name()

    while True:
        current_song = choose_song(songlist)
        game.run(current_song, playername)

if __name__ == '__main__':
    main()