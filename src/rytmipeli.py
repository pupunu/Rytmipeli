from song import load_songs
from game import run as game_run
from ui import *
from records_handler import chech_if_records_dir_exist, update_records


def main():
    chech_if_records_dir_exist()

    songlist = load_songs(directorypath='data/songs/')

    while True:
        playername = get_player_name()

        if playername:
            while True:
                current_song = choose_song(songlist)
                if current_song:
                    points = game_run(current_song, playername)

                    records = update_records(current_song, playername, points)
                    print_results(points, playername, current_song.name)
                    print_records(records[0], records[1])
                else:
                    break
        else:
            break


if __name__ == '__main__':
    main()
