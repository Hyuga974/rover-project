from Models.position import Position
from random import randint

class Obstacle:
    def __init__(self, planet):
        self.__position = Position(
            2, 3
            #randint(0, planet._Planet__size_x),
            #randint(0, planet._Planet__size_y),
        )

    