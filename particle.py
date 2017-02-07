import math


class Particle(object):
    """ A circular object with parameters """
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = 0
        self.angle = 0
        self.reflection = 0

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
