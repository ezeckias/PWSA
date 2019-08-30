class Memory:
    def __init__(self):
        self.memory = []
        self.create()

    # create memory
    def create(self):
        for x in range(1024):
            self.memory.append(0)

    # display memory
    def display(self,lim = 30):
        print('memory list: ')
        for z in range(lim):
            print(self.memory[z])

    def edit(self,pos, value):
        self.memory[pos] = value


class Interpreter(Memory):
    def __init__(self):
        super(Interpreter, self).__init__()
        self.pointer = 0
        self.instruction = ''
        self.error = 0

    # run the conditions
    def run(self,element):
        # print('element: ', element)
        if element == '+':
            self.edit(self.pointer, (self.memory[self.pointer] + 1))
        elif element == '-':
            self.edit(self.pointer, (self.memory[self.pointer] - 1))
        elif element == '>':
            self.pointer = self.pointer + 1
        elif element == '<':
            self.pointer = self.pointer - 1
        else:
            self.error = 1



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
        print(self.pointer)





program = Program()
program.start()

# print('the data from class')
# memory = Memory()
# memory.display()