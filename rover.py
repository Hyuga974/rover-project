class Rover():
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def checkLimitPlanet(self, planet):
        if self.x > planet.size_x:
            self.x = 0
        elif self.x < 0:
            self.x = planet.size_x
        elif self.y > planet.size_y:
            self.y = 0
        elif self.y < 0:
            self.y = planet.size_y
        pass

    def move(self, planet, direction):
        if direction == 'F':
            if self.orientation == 'N':
                self.y += 1
            elif self.orientation == 'E':
                self.x += 1
            elif self.orientation == 'S':
                self.y -= 1
            elif self.orientation == 'W':
                self.x -= 1
        elif direction == 'B':
            if self.orientation == 'N':
                self.y -= 1
            elif self.orientation == 'E':
                self.x -= 1
            elif self.orientation == 'S':
                self.y += 1
            elif self.orientation == 'W':
                self.x += 1
        self.checkLimitPlanet(planet)
        self.toString()
        pass

    def turn(self, rotation):
        if rotation == 'L':
            if self.orientation == 'N':
                self.orientation = 'W'
            elif self.orientation == 'E':
                self.orientation = 'N'
            elif self.orientation == 'S':
                self.orientation = 'E'
            elif self.orientation == 'W':
                self.orientation = 'S'
        elif rotation == 'R':
            if self.orientation == 'N':
                self.orientation = 'E'
            elif self.orientation == 'E':
                self.orientation = 'S'
            elif self.orientation == 'S':
                self.orientation = 'W'
            elif self.orientation == 'W':
                self.orientation = 'N'
        self.toString()
        pass

    def toString(self):
        return f"Rover is at {self.x}, {self.y} facing {self.orientation}"
