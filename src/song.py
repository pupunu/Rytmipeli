
class Song:
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

        with open(self.filename) as file:

            steps_have_started = False

            for line in file:
                line = line.strip()

                if steps_have_started:
                    self.steps.append(line)

                elif line == 'steps:':
                    steps_have_started = True
    
    def get_next_beat(self):
        self.current_beat += 1
        if self.current_beat < len(self.steps):
            return self.steps[self.current_beat]
        else:
            return False
 
        

