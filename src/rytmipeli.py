from song import *
import os
import game


def main():
    songlist = load_songs('data/songs/')
    playername = get_player_name()
    current_song = choose_song(songlist)
    game.main(current_song)


def get_player_name():
    print('Anna nimesi')
    name = input()
    if name == '':
        return 'Vierailija'
    else:
        return name

def choose_song(songlist):
    print('Biisit:')
    
    for song in songlist:
        print(song)
    print()

    while True:
        print('Valitse biisi')
        songname = input()
        if songname in songlist:
            songlist[songname].load_steps()
            return songlist[songname]
        print('epäkelpo nimi\n')


def load_songs(directorypath):
    songlist = {}

    dircontent = os.listdir(directorypath)
    for filename in dircontent:

        if '.txt' in filename:

            with open(directorypath + filename) as file:
                
                filename = file.name

                for line in file:

                    line_content = line.split(':')
                    key = line_content[0]
                    value = line_content[1].strip()

                    if key == 'name':
                        songname = value
                    elif key == 'audiofile':
                        audiofile = value
                    elif key == 'speed':
                        speed = int(value)
                        if speed <= 0:
                            raise negative_speed("Tiedoston " + filename + " nopeus on negatiivinen.")
                    elif key == 'offset':
                        offset = float(value)
                    elif key == 'steps':
                        break


            song = Song(songname, filename, directorypath + audiofile, speed, offset)

            songlist[songname] = song
    
    return songlist


if __name__ == '__main__':
    main()