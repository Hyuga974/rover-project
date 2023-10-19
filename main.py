from Models import rover
from Models import planet
from Models import instruction


def main():
    mars = planet.Planet(5, 5)
    curiosity = rover.Rover(1, 2, 'N')
    instructions = instruction.Instruction()

    while instructions.again:
        instructions.add_instruction()
        instructions.exec_commands(mars, curiosity)

if __name__ == '__main__':
    main()
