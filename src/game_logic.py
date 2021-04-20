BOX_Y = 50

def check_for_hits(row):
    for note in row:
        dist = is_hit(note.y)
        if dist:
            row.remove(note)
            return score(dist)

def is_hit(y):
    dist = abs(y - BOX_Y)
    if dist < 50:
        return dist
    else:
        return False

def score(dist):
    if dist < 10:
        return 'Brutaali'
    elif dist < 20:
        return 'Vaikea'
    elif dist < 30:
        return 'Normaali'
    elif dist < 40:
        return 'Helppo'
    else:
        return 'Heikko'

def check_floor_hit(note):
    if note.y < -note.height:
        return True, 'Oot huono'
    else:
        return False, ''

