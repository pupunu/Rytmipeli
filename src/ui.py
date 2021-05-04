# class UI:

# tänne toteutetaan visuaalinen
# käyttöliittymä nimen kysymiselle,
# biisin valinnalle ja tulosten näyttämiselle

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
            return songlist[songname]
        print('epäkelpo nimi\n')


def print_results(points, player, song):
    print('\n\nPisteet')
    print('Biisi:', song, '--- Pelaaja:', player)
    print('\nBrutaaleja:', points['brutal'])
    print('Vaikeita:', points['hard'])
    print('Normaaleja:', points['normal'])
    print('Helppoja:', points['easy'])
    print('Heikkoja:', points['weak'])
    print('\nYhteensä pisteitä:', points['total'], '\n\n')


def print_records(records, i):
    if i == 0:
        print('Sait uuden ennätyksen!!!\n')
    elif i > 0:
        print('Pääsit kymmenen parhaimman listalle!\n')
    
    for i in range(len(records)):
        current_record = records[i]
        print(str(i+1) + '.   ' + current_record[0] + '   ' + str(current_record[1]))

    print()
