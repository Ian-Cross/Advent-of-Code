from reused import arguments, read_file

PATH = "2ndDay/input.txt"

"""
Desc: Iterate through the opcodes found in the file, execute the opcode, and provide the answer found in address 0
Param: path: file path to datafile
"""
def part_1(path):
    # collect list of opcodes from the datafile
    opcodes = read_file(path or PATH,return_type=int,strip=True,split=",")

    # iterate through each opcode
    for opcode in opcodes:
        # initiate with pre "1202 program alarm" state
        opcode[1] = 12
        opcode[2] = 2
        # skip 4 to reach next instruction
        for i in range(0,len(opcode),4):
            if opcode[i] == 99:
                break

            # param 1 (i+1) as index for a
            # param2 (i+2) as index for b
            # param3 (i+3) as index for c

            # addition opcode, c = a + b
            if opcode[i] == 1:
                opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
            # multiplication opcode, c = a * b
            elif opcode[i] == 2:
                opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]

        print("Value left at address 0: %d" % opcode[0])

"""
Desc: Compute opcodes with different combinations of nouns and verbs to search for a desired output
Param: path: file path to datafile
"""
def part_2(path):
    # collect list of opcodes from the datafile
    opcodes = read_file(path or PATH,return_type=int,strip=True,split=",")

    """
    Desc: Initiate the opcode with the noun and verb, and execute the adjusted opcode returning the value in address 0
    Param: opcode: list of ints used to simulate an Intcode computer,
           noun: int to initiate address[1]
           verb: int to initiate address[2]
    """
    def comput_opcode(opcode = None,noun = 0, verb = 0):
        if not opcode:
            print("Please provide an opcode for computation")
            exit(0)
        # Initiate opcode
        opcode[1], opcode[2] = noun, verb

        # skip 4 to reach next instruction
        for i in range(0,len(opcode),4):
            if opcode[i] == 99:
                break

            # param 1 (i+1) as index for a
            # param2 (i+2) as index for b
            # param3 (i+3) as index for c

            # addition opcode, c = a + b
            if opcode[i] == 1:
                opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
            # addition opcode, c = a * b
            elif opcode[i] == 2:
                opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
        return opcode[0]

    # iterate through each opcode
    for opcode in opcodes:
        max_val = len(opcode)-1
        # Check all combinations of nouns and verbs from 0 - 99
        for noun in range(100):
            for verb in range(100):
                # check for overflow
                if noun > max_val or verb > max_val:
                    continue
                # compute the opcode with the current combination of noun, verb
                address_0 = comput_opcode(opcode.copy(),noun,verb)
                if (address_0 == 19690720):
                    print("Noun: %d, Verb: %d" % (noun,verb))
                    print("What is 100 * noun + verb = %d" % (100*noun+verb))

if __name__ == '__main__':
    arguments(part_1,part_2)
    print("\n")
