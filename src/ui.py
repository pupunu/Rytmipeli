def get_player_name():
    '''Funktio, jolla kysytään pelaajan nimeä

    Returns:
        Vierailija, jos pelaajanimeä ei kirjoiteta
        False, jos kirjoitetaan 'sulje'
        kirjoitetun merkkijonon muussa tapauksessa
    '''
    print("Anna nimesi.")
    print("Voit myös sulkea pelin komennolla 'sulje'\n")
    name = input()
    print()
    if name == '':
        return 'Vierailija'
    elif name == 'sulje':
        return False
    else:
        return name


def choose_song(songlist):
    ''' Funktio, joka kysyy mitä biisia halutaan pelata

    Args:
        songlist: lista pelissä olevista kappaleista

    Returns:
        valinnan niminen biisi, jos sellainen listasta löytyy
        False, jos valinta on 'poistu'
    '''
    print('Biisit:')

    for song in songlist:
        print(song)
    print()

    while True:
        print('Valitse biisi')
        print("Voit myös poistua pelistä komennolla 'poistu'\n")

        songname = input()
        print()
        if songname in songlist:
            return songlist[songname]
        elif songname == 'poistu':
            return False
        print('epäkelpo nimi\n')


def print_results(points, player, song):
    ''' Funktio joka tulostaa pelissä saadut pisteet

    Args:
        points: dicti, jossa jokaiselle arvosanatyypille kuinka monta saatu sekä kokonaispistemäärä
        player: pelaajan nimi
        song: minkä biisin bisteet ovat kyseessä
    '''
    print('\n\nPisteet')
    print('Biisi:', song, '--- Pelaaja:', player)
    print('\nBrutaaleja:', points['brutal'])
    print('Vaikeita:', points['hard'])
    print('Normaaleja:', points['normal'])
    print('Helppoja:', points['easy'])
    print('Heikkoja:', points['weak'])
    print('\nYhteensä pisteitä:', points['total'], '\n\n')


def print_records(records, i):
    '''Funktio, joka tulostaa näytölle top 10 -pelaajan pisteet

    Args:
        records: lista tupleista muotoa (pelaajan nimi, pistemäärä)
        i: monesko tämänhetkinen pelaaja on ollut listalla. jos pelaaja ei päässyt top 10, i == -1
    '''
    if i == 0:
        print('Sait uuden ennätyksen!!!\n')
    elif i > 0:
        print('Pääsit kymmenen parhaimman listalle!\n')
    
    for i in range(len(records)):
        current_record = records[i]
        print(str(i+1) + '.   ' + current_record[0] + '   ' + str(current_record[1]))

    print()
