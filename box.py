from random import randint


class Box:
    def __init__(self, balls):
        self.storage = balls

    def reset(self):
        self.balls = self.storage[:]

    def pick(self):
        r = randint(0, len(self.balls) - 1)
        return self.balls.pop(r)
