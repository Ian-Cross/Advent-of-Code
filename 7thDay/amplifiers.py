from reused import arguments, read_file
from itertools import permutations

PATH="7thDay/input.txt"
opcode=None

def as_index(a):
    global opcode
    return opcode[opcode[a]];


def as_value(a):
    global opcode
    return opcode[a];


def retrieve_param(operation = None,a = None,b = None):
    if a is not None and b is not None:
        return (as_index(a) if operation[2] == "0" else as_value(a),
                as_index(b) if operation[1] == "0" else as_value(b))
    elif b is None:
        return as_index(a) if operation[2] == "0" else as_value(a)


"""
Desc:
Param: path: file path to pasword range
"""
def part_1(path):
    global opcode
    opcodes = read_file(path or PATH,return_type=int,strip=True,split=",")
    highest_output = 0
    best_phase = []

    """
    Desc: Execute the opcode returning the computer list
    Param: opcode: list of ints used to simulate an Intcode computer,
    """
    def comput_opcode(phase,input):
        global opcode
        if not opcode:
            print("Please provide an opcode for computation")
            exit(0)

        operation = ""
        halted = False
        inputs = 0
        i = 0

        while not halted:
            if opcode[i] == 99:
                halted = True

            operation = str(opcode[i])
            while len(operation) < 5:
                operation = "0" + operation

            # addition opcode, c = a + b
            if operation[3:] == "01":
                a,b = retrieve_param(operation,i+1,i+2)
                opcode[as_value(i+3)] = a + b
                i+=4
            # addition opcode, c = a * b
            elif operation[3:] == "02":
                a,b = retrieve_param(operation,i+1,i+2)
                opcode[as_value(i+3)] = a * b
                i+=4
            elif operation[3:] == "03":
                if inputs == 0:
                    opcode[as_value(i+1)] = int(phase)
                    inputs+=1
                elif inputs == 1:
                    opcode[as_value(i+1)] = int(input)
                    inputs+=1
                else:
                    print("Too Many Inputs")
                    exit(1)
                i+=2
            elif operation[3:] == "04":
                a = retrieve_param(operation,i+1)
                return(a)
                i+=2
            elif operation[3:] == "05":
                a,b = retrieve_param(operation,i+1,i+2)
                i = i+3 if a == 0 else b
            elif operation[3:] == "06":
                a,b = retrieve_param(operation,i+1,i+2)
                i = b if a == 0 else i+3
            elif operation[3:] == "07":
                a,b = retrieve_param(operation,i+1,i+2)
                opcode[as_value(i+3)] = 1 if  a < b else 0
                i+=4
            elif operation[3:] == "08":
                a,b = retrieve_param(operation,i+1,i+2)
                opcode[as_value(i+3)] = 1 if  a == b else 0
                i+=4

    for code in opcodes:
        for phase_setting in list(permutations([0,1,2,3,4])):
            prev_input = 0
            for phase in phase_setting:
                opcode = code.copy()
                prev_input = comput_opcode(phase,prev_input)
            if prev_input > highest_output:
                highest_output = prev_input
    print ( highest_output )

def part_2(path):
    pass


if __name__ == '__main__':
    arguments(part_1,part_2)
    print("\n")
