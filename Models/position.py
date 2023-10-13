from Models.coordinate import Coordinate

class Position:
    def __init__(self, x, y) -> None:
        self.__x = Coordinate(x)
        self.__y = Coordinate(y)
