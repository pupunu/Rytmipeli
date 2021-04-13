from song import *


class Catalog:
    def __init__(self):
        self.songlist = {}

    def does_song_exist(self, songname):
        return songname in self.songlist


    def load_songs(self, directorypath):

        dircontent = os.listdir(directorypath)
        for filename in dircontent:

            if '.txt' in filename:

                with open(directorypath + filename) as file:
                    filename = file.name

                    for line in file:
                        line_content = line.split(':')
                        if line_content[0] == 'name':
                            songname = line_content[1].strip()

                song = Song(songname, filename)

                self.songlist[songname] = song


    def get_song(self, songname):
        if songname in self.songlist:
            return self.songlist[songname]
        return False

    def list_songs(self):
        for song in self.songlist:
            print(song)
        print()