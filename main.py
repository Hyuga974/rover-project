import rover
import planet

def main():
    mars = planet.Planet(5, 5)
    curiosity = rover.Rover(1, 2, 'N')

    while True:
        print(f'Curiosity is at ({curiosity.x}, {curiosity.y}) facing {curiosity.orientation}')
        command = input('Enter command: ')
        if command == 'F':
            curiosity.move(mars, 'F')
        elif command == 'B':
            curiosity.move(mars, 'B')
        elif command == 'L':
            curiosity.turn('L')
        elif command == 'R':
            curiosity.turn('R')
        elif command == 'Q':
            break
        else:
            print('Invalid command')
        pass

if __name__ == '__main__':
    main()
