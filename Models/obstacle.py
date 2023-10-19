from Models.position import Position
from random import randint

class Obstacle:
    def __init__(self, planet):
        self.__position = Position(
            randint(0, planet._Planet__size_x),
            randint(0, planet._Planet__size_y),
        )

    