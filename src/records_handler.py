import os

def chech_if_records_dir_exist():
    '''Funktio joka tarkistaa onko ennätyshakemisto oikeassa paikassa ja luo sellaisen sen puuttuessa
    '''
    if not os.path.isdir("data/records"):
        os.mkdir("data/records")


def make_new_record_file(song):
    '''Funktio joka luo uuden ennätystiedoston biisille

    Args:
        song: mille kappaleelle ennätystiedosto luodaan
    '''
    path = 'data/records/' + song.name + '.txt'

    file = open(path, 'x')
    file.close()

    records = []
    for i in range(10):
        records.append(('---', 0))

    set_song_record(song, records)


def get_song_record(song):
    '''Funktio, joka lukee tiedostosta biisin ennätykset

    Args:
        song: minkä kappaleen ennätykset halutaan

    Returns:
        lista kappaleen ennätyksistä
    '''
    path = 'data/records/' + song.name + '.txt'

    if not os.path.isfile(path):
        make_new_record_file(song)

    records = []
    with open(path) as file:
        #luetaan enkat tiedostosta
        for line in file:
            line_content = line.split(':')
            record = line_content[0], int(line_content[1])
            records.append(record)

    return records


def set_song_record(song, new_records):
    '''Funktio, jolla uudet ennätykset kirjataan tiedostoon
    
    Args:
        song: kappale jolle ennätys lisätään
        new_records: uudet ennätykset, jotka tiedostoon kirjataan
    '''
    path = 'data/records/' + song.name + '.txt'

    file = open(path, 'w')
    for record in new_records:

        file.write(record[0] + ':' + str(record[1]) + '\n')
    
    file.close()


def update_records(song, playername, points):
    '''Funktio jolla päivitetään uusi tulos ennätyksiin

    Args:
        song: mille kappaleelle uusi tulos on
        playername: merkkijono, kuka tuloksen on saanut
        points: dictionary missä tulokset

    Returns:
        new_records: lista, jossa top 10 pisteet tupleina (pelaajanimi, kokonaispistemäärä)
        new_result_i: monennesko uusi tulos on ollut top 10 listalla. jos tulos ei ole päässyt listalle, tämä on -1
    '''
    old_records = get_song_record(song)

    new_result = playername, points['total']

    new_records = [] 

    new_result_i = -1

    for i in range(len(old_records)):
        if old_records[i][1] >= new_result[1]:
            new_records.append(old_records[i])

        elif old_records[i][1] < new_result[1] and new_result_i < 0:
            new_records.append(new_result)
            new_result_i = i

        else:
            new_records.append(old_records[i-1])


    set_song_record(song, new_records)


    return new_records, new_result_i
