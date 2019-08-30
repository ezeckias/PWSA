from Interpreter import Interpreter

class Program(Interpreter):
    def __init__(self):
        super(Program, self).__init__()

    # super()
    def start(self):
        print('welcome to ..:')
        # while self.memory[self.pointer] == 0:
        self.instruction = input(': ')
        self.program_start()




program = Program()
program.start()