class Rover():
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def move(self, planet, direction):
        movements = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0)
        }

        opposites = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}

        if direction == 'F':
            dx, dy = movements[self.orientation]
        elif direction == 'B':
            dx, dy = movements[opposites[self.orientation]]
        else:
            raise ValueError("Invalid direction")

        self.x += dx
        self.y += dy
        self.check_limit_planet(planet)
        self.toString()

    def turn(self, rotation):
        rotations = {
            'N': {'L': 'W', 'R': 'E'},
            'E': {'L': 'N', 'R': 'S'},
            'S': {'L': 'E', 'R': 'W'},
            'W': {'L': 'S', 'R': 'N'}
        }

        if rotation in ['L', 'R']:
            self.orientation = rotations[self.orientation][rotation]
        else:
            raise ValueError("Invalid rotation")
        self.toString()

    def check_limit_planet(self, planet):
        if self.x > planet.size_x:
            self.x = 0
        elif self.x < 0:
            self.x = planet.size_x
        elif self.y > planet.size_y:
            self.y = 0
        elif self.y < 0:
            self.y = planet.size_y

    def toString(self):
        print(f"Rover is at {self.x}, {self.y} facing {self.orientation}")
