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
            print(self.memory[z],end=' ')
        print('\n')
    def edit(self,pos, value):
        self.memory[pos] = value
