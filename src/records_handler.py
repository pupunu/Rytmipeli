import os

def chech_if_records_dir_exist():
    if not os.path.isdir("data/records"):
        os.mkdir("data/records")


def make_new_record_file(song):
    path = 'data/records/' + song.name + '.txt'

    #luodaan tiedosto enkkoja varten
    file = open(path, 'x')
    file.close()

    # luodaan lista enkoista
    records = []
    for i in range(10):
        records.append(('---', 0))

    set_song_record(song, records)


#lukee tiedostosta enkat
def get_song_record(song):
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


#kirjoittaa uudet enkat tiedostoon
def set_song_record(song, new_records):
    path = 'data/records/' + song.name + '.txt'

    file = open(path, 'w')
    for record in new_records:

        file.write(record[0] + ':' + str(record[1]) + '\n')
    
    file.close()


def update_records(song, playername, points):
    old_records = get_song_record(song)


    #uusi pelitulos
    new_result = playername, points['total']

    new_records = [] 

    new_result_i = -1

    for i in range(len(old_records)):
        #jos enkka on isompi kuin uusi entry
        if old_records[i][1] >= new_result[1]:
            new_records.append(old_records[i])

        #jos uusi entry on isompi ensimmäistä kertaa
        elif old_records[i][1] < new_result[1] and new_result_i < 0:
            new_records.append(new_result)
            new_result_i = i

        
        #enkan lisäämisen jälkeen
        else:
            new_records.append(old_records[i-1])


    set_song_record(song, new_records)


    return new_records, new_result_i
