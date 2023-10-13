from Models.position import Position
from Models.orientation import Orientation


class Rover:
    def __init__(self, x, y, orientation):
        self.__position = Position(x, y)
        self.__orientation = Orientation(orientation)

    def move(self, planet, direction):
        self.__position = self.__orientation.update_position(direction, self.__position)
        self = planet.check_limit_planet(self)
        self.to_string()

    def turn(self, rotation):
        self.__orientation = self.__orientation.update_orientation(rotation)
        self.to_string()

    def to_string(self):
        print(
            f"Rover is at {self.__position._Position__x._Coordinate__value}, {self.__position._Position__y._Coordinate__value} facing {self.__orientation._Orientation__orientation}")
