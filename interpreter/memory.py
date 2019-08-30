
# class Memory:
#     def __init__(self):
#         self.memory = []
    
#     def create(self):
#         for x in range(1024):
#             self.memory[x] = 0
    
pointer = 0
instruction = ''
error = 0

memory = []
for x in range(1024):
    memory.append(0)
# print(memory)




#  interpretor
# def compile(x, pointer):
#     if x == '+':
#         memory[pointer] += 1
#     elif x == '-':
#         memory[pointer] -= 1
#     elif x == '>':
#         pointer += 1
#     elif x == '<':
#         pointer -= 1
#     else:
#         error = 1

while memory[pointer] == 0:
    instruction = input(': ')
    inst_size = len(instruction)

    # loop through the instructions
    for x in range(inst_size):
        # compile(instruction[x], pointer)
        # print(instruction[x])
        if instruction[x] == '+':
            memory[pointer] = memory[pointer] + 1
        elif instruction[x] == '-':
            memory[pointer] = memory[pointer] - 1
        elif instruction[x] == '>':
            pointer = pointer + 1
        elif instruction[x] == '<':
            pointer = pointer - 1
        else:
            error = 1

    print('------------------------- memory')
    for z in range(10):
        print(memory[z])
    print('------------------------ pointer: ', pointer)
# print some samples
# for z in range(30):
#     print(memory[z])




# mem = Memory()
# mem.create()
# print(mem.memory)