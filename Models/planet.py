from Models.obstacle import Obstacle

class Planet:
    def __init__(self, size_x, size_y):
        self.__size_x = size_x
        self.__size_y = size_y
        self.__obstacles = [
            Obstacle(self) #for _ in range(size_x*size_y//10)
        ]

    def check_limit_planet(self, rover):
        if rover._Rover__position._Position__x._Coordinate__value > self.__size_x:
            rover._Rover__position._Position__x._Coordinate__value = 0
        elif rover._Rover__position._Position__x._Coordinate__value < 0:
            rover._Rover__position._Position__x._Coordinate__value = self.__size_x
        elif rover._Rover__position._Position__y._Coordinate__value > self.__size_y:
            rover._Rover__position._Position__y._Coordinate__value = 0
        elif rover._Rover__position._Position__y._Coordinate__value < 0:
            rover._Rover__position._Position__y._Coordinate__value = self.__size_y
        return rover

    def is_obstacle_at_position(self, position) :
        for obstacle in self.__obstacles :
            if obstacle._Obstacle__position._Position__x._Coordinate__value == position._Position__x._Coordinate__value and obstacle._Obstacle__position._Position__y._Coordinate__value == position._Position__y._Coordinate__value :
                return True
        return False