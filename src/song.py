from os import listdir


class Song:
    '''Luokka, jonka avulla biisien tiedostonimet, nimet, askeleet ja musiikkitiedostot löytyvät ohjelmalle helposti

    Attributes:
        name: biisin nimi
        filename: biisin tiedot sisältävän tiedoston tiedostonimi
        audiofile: biisin musiikkitiedoston tiedostonimi
        speed: biisin nopeus muodossa iskua minuttissa
        offset: kuinka paljon askelten/musiikin tulee odottaa, että askeleet alkavat musiikin kannalta oikeassa kohtaa
    '''

    def __init__(self, name, filename, audiofile, speed, offset):
        self.name = name
        self.filename = filename
        self.audiofile = audiofile
        self.steps = []
        self.speed = speed
        self.current_beat = -1
        self.offset = offset

    def __str__(self):
        return self.name

    def load_steps(self):
        '''Ladataan tiedostosta biisin nuotit
        '''

        with open(self.filename) as file:

            steps_have_started = False

            for line in file:
                line = line.strip()

                if steps_have_started:
                    self.steps.append(line)

                elif line == 'steps:':
                    steps_have_started = True

    def get_next_beat(self):
        '''Tällä metodilla pelin pyöriessä saa aina seuraavan tahdin nuotit.
        
        Returns:
            tahdin nuotit, jos askeleita nuotteja vielä riittää
            False, jos nuotit ovat loppuneet (eli biisi on loppu) 
        '''
        self.current_beat += 1
        if self.current_beat < len(self.steps):
            return self.steps[self.current_beat]
        else:
            return False


def load_songs(directorypath):
    ''' Funtkio, jolla ladataan pelin alussa tiedostoista biisit.

    Args:
        directorypath: polku mistä biisit löytyvät
    '''

    songlist = {}

    dircontent = listdir(directorypath)
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
                            raise NegativeSpeed(
                                "Tiedoston " + filename + " nopeus on negatiivinen.")
                    elif key == 'offset':
                        offset = float(value)
                    elif key == 'steps':
                        break

            song = Song(songname, filename, directorypath +
                        audiofile, speed, offset)

            songlist[songname] = song

    return songlist
