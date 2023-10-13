from Models.position import Position


class Orientation:
    def __init__(self, orientation):
        self.__orientation = orientation
        self.__movements = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0)
        }
        self.__opposites = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
        self.__rotations = {
            'N': {'L': 'W', 'R': 'E'},
            'E': {'L': 'N', 'R': 'S'},
            'S': {'L': 'E', 'R': 'W'},
            'W': {'L': 'S', 'R': 'N'}
        }

    def update_position(self, direction, position):
        if direction == 'F':
            dx, dy = self.__movements[self.__orientation]
        elif direction == 'B':
            dx, dy = self.__movements[self.__opposites[self.__orientation]]
        else:
            raise ValueError("Invalid direction")
        dx += position._Position__x._Coordinate__value
        dy += position._Position__y._Coordinate__value
        return Position(dx, dy)

    def update_orientation(self, rotation):
        rotations = self.__rotations

        if rotation in ['L', 'R']:
            return Orientation(rotations[self.__orientation][rotation])
        else:
            raise ValueError("Invalid rotation")
