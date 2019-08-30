from Memory import Memory

class Interpreter(Memory):
    def __init__(self):
        super(Interpreter, self).__init__()
        self.pointer = 0
        self.s_pointer = 0
        self.instruction = ''
        self.error = 0
        self.execute = True
        self.positions = []
        self.symbols = ['[',']']
        self.conditions = {
                    '+': self.addOne,
                    '-': self.removeOne,
                    '>': self.nextPoint,
                    '<': self.prevPoint,
                    '~': self.inverse,
                    '.': self.memory_curent,
                    ',': self.related_char,
                    '?': self.edit_statement
                }


    # this will be used for the closing tags
    def place(self,element, size):
        if size < 0:
            pass
        else:
            # check if the current position has the lase tltmtny
            if len(self.positions[size]) == 1:
                self.positions[size].append(element)
            else:
                self.place(element, size -1)


    # finding brackets in a program
    def set_pos(self):
        # print('setting position')
        for x in range(len(self.instruction)):
            # print('curent instriction: ',self.instruction[x])
            if self.instruction[x] == '[':
                temp = []
                temp.append(x)
                self.positions.append(temp)
            elif self.instruction[x] == ']':
                self.place(x, len(self.positions) -1)


    # this function will return the answer with the position
    def search(self,element):
        for x in self.positions:
            if element in x:
                return [True,x]
        return [False,[]]

    def nextPoint(self):
        self.pointer = self.pointer + 1

    def prevPoint(self):
        self.pointer = self.pointer - 1

    def addOne(self):
        self.edit(self.pointer, (self.memory[self.pointer] + 1))

    def removeOne(self):
        self.edit(self.pointer, (self.memory[self.pointer] - 1))

    def inverse(self):
        num = self.memory[self.pointer] * (-1)
        self.edit(self.pointer, num)

    def memory_curent(self):
        print("the curent memory is:", self.memory[self.pointer])

    def related_char(self):
        print('the character related to ', self.memory[self.pointer] , ' is ', self.characters[self.memory[self.pointer]])

    def edit_statement(self):
        indata = int(input('enter the number: '))
        self.memory[self.pointer] = indata

    # run the conditions
    def run(self,element):
        if element in self.conditions:
            self.conditions[element]()

    def program_start(self):
        self.set_pos()
        while self.execute:

            # set back the instruction
            # if len(self.instruction) >= self.s_pointer:
            #     inst_count = self.s_pointer -1
            # else:
            #     inst_count = self.s_pointer


            if self.instruction[self.s_pointer] in self.symbols:
                # change the instruction point
                if self.instruction[self.s_pointer] == '[':
                    # chack the memory
                    if self.memory[self.pointer] > 0:
                        self.s_pointer = self.s_pointer + 1 # shitano
                    else:
                        last_position = self.search(self.s_pointer)
                        self.s_pointer = last_position[1][1] + 1
                elif self.instruction[self.s_pointer] == ']':
                    start_position = self.search(self.s_pointer)
                    self.s_pointer = start_position[1][0]

            else:
                # run the statement
                self.run(self.instruction[self.s_pointer])

                # change the positions
                if self.s_pointer > len(self.instruction)-2:
                    self.execute = False
                else:
                    self.s_pointer = self.s_pointer + 1


        print('program terinated')
        print('----------- memory:')
        print(self.display())
        print('instructions: ', self.instruction)

        print('----------- pointer:')
        print(self.pointer)

        print('----------- program brackets:')
        print(self.positions)


