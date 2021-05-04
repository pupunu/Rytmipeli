from song import load_songs
from game import run as game_run
from ui import *
from records_handler import chech_if_records_dir_exist, update_records


def main():
    chech_if_records_dir_exist()

    songlist = load_songs(directorypath='data/songs/')
    playername = get_player_name()

    while True:
        current_song = choose_song(songlist)
        points = game_run(current_song, playername)

        records = update_records(current_song, playername, points)
        print_results(points, playername, current_song.name)
        print_records(records[0], records[1])


if __name__ == '__main__':
    main()
