class Memory:
    def __init__(self):
        self.memory = []
        self.characters = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
