class Song:
    def __init__(self, name, songfile):
        self.name = name
        self.songfile = songfile

    def __str__(self):
        return self.name

    def load_steps():
        return



class Catalog:
    def __init__(self):
        self.songlist = {}

    def does_song_exist(self, songname):
        if songname in self.songlist:
            return True
        return False


    def load_songs(self, filename):
        with open(filename) as file:
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

        