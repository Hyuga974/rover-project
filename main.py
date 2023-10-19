from Models import rover
from Models import planet
from Models import instruction
from Models import position
from Models import obstacle


def main():
    mars = planet.Planet(5, 5, [obstacle.Obstacle(None, position.Position(5, 5))])
    #print(obstacle._Obstacle__position._Position__x._Coordinate__value)
    curiosity = rover.Rover(0, 0, 'N')
    instructions = instruction.Instruction()

    while instructions.again:
        instructions.add_instruction()
        instructions.exec_commands(mars, curiosity)

if __name__ == '__main__':
    main()
