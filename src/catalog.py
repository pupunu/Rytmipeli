from song import *


class Catalog:
    def __init__(self):
        self.songlist = {}


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

    def list_songs(self):
        return list(self.songlist.keys())
