class Planet:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def check_limit_planet(self, rover):
        if rover._Rover__position._Position__x._Coordinate__value > self.size_x:
            rover._Rover__position._Position__x._Coordinate__value = 0
        elif rover._Rover__position._Position__x._Coordinate__value < 0:
            rover._Rover__position._Position__x._Coordinate__value = self.size_x
        elif rover._Rover__position._Position__y._Coordinate__value > self.size_y:
            rover._Rover__position._Position__y._Coordinate__value = 0
        elif rover._Rover__position._Position__y._Coordinate__value < 0:
            rover._Rover__position._Position__y._Coordinate__value = self.size_y
        return rover
