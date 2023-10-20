from Models.position import Position
from Models.orientation import Orientation

#Entitté (candidat OV)
class Rover:
    def __init__(self, x, y, orientation):
        #Identité du ROVER
        self.__position = Position(x, y)
        self.__orientation = Orientation(orientation)

    def move_forward(self, planet):
        self.__position, is_obstacle = self.__orientation.update_position('F', self.__position, planet)
        self.to_string()
        return is_obstacle
        
    def move_backward(self, planet):
        self.__position, is_obstacle = self.__orientation.update_position('B', self.__position, planet)
        self.to_string()
        return is_obstacle

    def turn_left(self):
        self.__orientation = self.__orientation.update_orientation('L')
        self.to_string()
        
    def turn_right(self):
        self.__orientation = self.__orientation.update_orientation('R')
        self.to_string()

    def to_string(self):
        print(
            f"Rover is at {self.__position._Position__x._Coordinate__value}, {self.__position._Position__y._Coordinate__value} facing {self.__orientation._Orientation__orientation}")
