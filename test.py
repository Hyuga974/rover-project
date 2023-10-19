import unittest
from Models.rover import Rover
from Models.planet import Planet


class TestRover(unittest.TestCase):
    def setUp(self):
        self.planet = Planet(5, 5)
        self.rover = Rover(0, 0, 'N')

    def testForward(self):
        self.rover.move(self.planet, 'F')
        self.assertEqual(self.rover._Rover__position
                         ._Position__x
                         ._Coordinate__value, 0)
        self.assertEqual(self.rover._Rover__position._Position__y._Coordinate__value, 1)
        self.assertEqual(self.rover._Rover__orientation._Orientation__orientation, 'N')

    def testForwardOutOfLimit(self):
        self.rover = Rover(0, 5, 'N')

        self.rover.move(self.planet, 'F')
        self.assertEqual(self.rover._Rover__position._Position__x._Coordinate__value, 0)
        self.assertEqual(self.rover._Rover__position._Position__y._Coordinate__value, 0)
        self.assertEqual(self.rover._Rover__orientation._Orientation__orientation, 'N')

    def testBackwardOutOfLimit(self):
        self.rover.move(self.planet, 'B')
        self.assertEqual(self.rover._Rover__position._Position__x._Coordinate__value, 0)
        self.assertEqual(self.rover._Rover__position._Position__y._Coordinate__value, 5)
        self.assertEqual(self.rover._Rover__orientation._Orientation__orientation, 'N')

    def testBackward(self):
        self.rover = Rover(0, 4, 'N')

        self.rover.move(self.planet, 'B')
        self.assertEqual(self.rover._Rover__position._Position__x._Coordinate__value, 0)
        self.assertEqual(self.rover._Rover__position._Position__y._Coordinate__value, 3)
        self.assertEqual(self.rover._Rover__orientation._Orientation__orientation, 'N')

    def testTurnRight(self):
        self.rover.turn('R')
        self.assertEqual(self.rover._Rover__orientation._Orientation__orientation, 'E')

    def testTurnLeft(self):
        self.rover.turn('L')
        self.assertEqual(self.rover._Rover__orientation._Orientation__orientation, 'W')


if __name__ == '__main__':
    unittest.main()
