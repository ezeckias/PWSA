from Memory import Memory

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