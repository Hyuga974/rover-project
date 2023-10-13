from Models import rover
from Models import planet
from Models import orientation


def main():
    mars = planet.Planet(5, 5)
    curiosity = rover.Rover(1, 2, 'N')

    while True:
        command = input('Enter command: ')
        if command == 'F':
            curiosity.move_forward(mars)
        elif command == 'B':
            curiosity.move_backward(mars)
        elif command == 'L':
            curiosity.turn_left()
        elif command == 'R':
            curiosity.turn_right()
        elif command == 'Q':
            break
        else:
            print('Invalid command')
        pass


if __name__ == '__main__':
    main()
