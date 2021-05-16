BOX_Y = 50


def check_for_hits(row):
    ''' Funktio jonka avulla tarkistetaan onko nuotteja
        osumaetäisyydellä ja jos on, niin kuinka tarkka
        osuma on kyseessä

    Args:
        row: lista, jonka alkiot ovat nuottiolioita.

    Returns:
        None, jos rivillä ei ole yhtäkään nuottia osumaetäisyydellä
        'brutal', jos nuotin etäisyys täysosumasta on alle 10
        'hard', jos nuotin etäisyys täysosumasta on 10-19
        'normal', jos nuotin etäisyys on 20-29
        'easy' jos nuotin etäisyys on 30-39
        'weak', jos etäisyys on 40-49
    '''
    for note in row:
        dist = is_hit(note.y)
        if dist:
            row.remove(note)
            return get_score(dist)


def is_hit(height):
    ''' Funktio tarkistaa onko osuma tapahtunut nuotin y-koordinaatin perusteella

    Args:
        y: testattavan nuotin y-koordinaatti

    Returns:
        nuotin etäisyys täydellisestä osumasta jos, etäisyys on alle 50
        False, jos etäisyys on 50 tai yli.
    '''

    dist = abs(height - BOX_Y)
    if dist < 50:
        return dist
    return False


def get_score(dist):
    '''Funktio määrittää mikä arvosana osumasta on saatu:

    Args:
        dist: nuotin etäisyys optimaaliseen osumakohtaan

    Returns:
        'brutal', jos nuotin etäisyys täysosumasta on alle 10
        'hard', jos nuotin etäisyys täysosumasta on 10-19
        'normal', jos nuotin etäisyys on 20-29
        'easy' jos nuotin etäisyys on 30-39
        'weak', jos etäisyys on 40-49
    '''

    if dist < 10:
        return 'brutal'
    elif dist < 20:
        return 'hard'
    elif dist < 30:
        return 'normal'
    elif dist < 40:
        return 'easy'
    return 'weak'


def check_floor_hit(note):
    '''Funktio tarkistaa onko nuotti poistunut tippunut alas asti (peliruudulta pois)

    Args:
        note: nuotti, jonka poistumista tarkistellaan

    Returns:
        True ja 'oot huono', jos nuotti on mennyt kokonaan
            pelaajalta ohi ja siirtynyt pois pelikentältä.
        False ja '' jos yksikään nuotti on edelleen pelikentällä
    '''

    if note.y < -note.height:
        return True, 'Oot huono'
    return False, ''


def give_points(points_dict, score):
    '''Funktio päivittää pelaajan pisteet

    Args:
        points_dict: dictionary, johon pelaajan pisteet on tallennettu
        score: pisteen tyyppi, joka päivitetään
    '''
    
    points_dict[score] += 1
    points = 0
    if score == 'brutal':
        points = 100
    elif score == 'hard':
        points = 50
    elif score == 'normal':
        points = 25
    elif score == 'easy':
        points = 10
    elif score == 'weak':
        points = 1
    points_dict['total'] += points
