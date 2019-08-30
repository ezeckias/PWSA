from Interpreter import Interpreter

class Program(Interpreter):
    def __init__(self):
        super(Program, self).__init__()

    # super()
    def start(self):
        while self.memory[self.pointer] == 0:
            self.instruction = input(': ')
            inst_size = len(self.instruction)

            for x in range(inst_size):
                self.run(self.instruction[x])
                # print(self.instruction[x])
            print('--------')
        self.display()
        print('pointer: ',self.pointer)





program = Program()
program.start()