input_file = open("input.txt",'r')

opcode = [int(item) if item.isnumeric else -1 for item in input_file.read().strip().split(",")]

def comput_opcode(noun = 0, verb = 0):
    mem = opcode.copy()
    mem[1] = noun
    mem[2] = verb
    for i in range(0,len(mem),4):
        if mem[i] == 99:
            break

        if mem[i] == 1:
            mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
        elif mem[i] == 2:
            mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
    return mem


max_val = len(opcode)-1
for i in range(100):
    for j in range(100):
        if i > max_val or j > max_val:
            continue
        mem = comput_opcode(i,j)
        if (mem[0] == 19690720):
            print("Noun: %d, Verb: %d" % (i,j))
            print("What is 100 * noun + verb = %d" % (100*i+j))
            exit(0)
