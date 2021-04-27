BOX_Y = 50


def check_for_hits(row):
    for note in row:
        dist = is_hit(note.y)
        if dist:
            row.remove(note)
            return get_score(dist)


def is_hit(y):
    dist = abs(y - BOX_Y)
    if dist < 50:
        return dist
    return False


def get_score(dist):
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
    if note.y < -note.height:
        return True, 'Oot huono'
    return False, ''


def give_points(points_dict, score):
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
