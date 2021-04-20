#class UI:

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
            songlist[songname].load_steps()
            return songlist[songname]
        print('epäkelpo nimi\n')