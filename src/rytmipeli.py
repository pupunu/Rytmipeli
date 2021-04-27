from song import load_songs
from game import run as game_run
from ui import *


def main():
    songlist = load_songs(directorypath='data/songs/')
    playername = get_player_name()

    while True:
        current_song = choose_song(songlist)
        points = game_run(current_song, playername)
        print_results(points, playername, current_song.name)


if __name__ == '__main__':
    main()
