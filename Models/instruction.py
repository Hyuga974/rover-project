class Instruction:
    def __init__(self):
        self.__instruction_order = []
        self.__forward = 'F'
        self.__backward = 'B'
        self.__left = 'L'
        self.__right = 'R'

    def add_instruction(self):
        commands_string = input('Enter commands: ').replace(" ", "")
        commands = list(commands_string)
        is_valid = all(element == self.__forward or element == self.__backward or element == self.__left or element == self.__right for element in commands)
        
        if is_valid :
            for command in commands :
                self.__instruction_order.append(command)
        else:
            print('Invalid command list')
        pass

    def exec_commands(self, planet, rover):
        for command in self.__instruction_order:
            if command == 'F':
                rover.move_forward(planet)
            elif command == 'B':
                rover.move_backward(planet)
            elif command == 'L':
                rover.turn_left()
            elif command == 'R':
                rover.turn_right()