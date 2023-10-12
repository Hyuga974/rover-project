import unittest
from Models.rover import Rover
from Models.planet import Planet

class TestRover(unittest.TestCase):
    def setUp(self):
        self.planet = Planet(5, 5)
        self.rover = Rover(0, 0, 'N')

    def testForward(self):
        self.rover.move(self.planet, 'F')
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 1)
        self.assertEqual(self.rover.orientation, 'N')

    def testForwardOutOfLimit(self):
        self.rover = Rover(0, 5, 'N')

        self.rover.move(self.planet, 'F')
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 0)
        self.assertEqual(self.rover.orientation, 'N')

    def testBackwardOutOfLimit(self):
        self.rover.move(self.planet, 'B')
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 5)
        self.assertEqual(self.rover.orientation, 'N')

    def testBackward(self):
        self.rover = Rover(0, 4, 'N')

        self.rover.move(self.planet, 'B')
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 3)
        self.assertEqual(self.rover.orientation, 'N')

    def testTurnRight(self):
        self.rover.turn('R')
        self.assertEqual(self.rover.orientation, 'E')

    def testTurnLeft(self):
        self.rover.turn('L')
        self.assertEqual(self.rover.orientation, 'W')

if __name__ == '__main__':
    unittest.main()
