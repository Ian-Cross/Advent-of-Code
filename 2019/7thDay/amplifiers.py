from reused import arguments, read_file
from itertools import permutations

PATH="7thDay/test.txt"
opcode=None

def as_index(opcode,a):
    return opcode[opcode[a]];


def as_value(opcode,a):
    return opcode[a];


def retrieve_param(opcode, operation = None,a = None,b = None):
    if a is not None and b is not None:
        return (as_index(opcode,a) if operation[2] == "0" else as_value(opcode,a),
                as_index(opcode,b) if operation[1] == "0" else as_value(opcode,b))
    elif b is None:
        return as_index(opcode,a) if operation[2] == "0" else as_value(opcode,a)


"""
Desc: Execute the opcode returning the computer list
Param: opcode: list of ints used to simulate an Intcode computer,
"""
def comput_opcode(opcode,phase,input_val):
    if not opcode:
        print("Please provide an opcode for computation")
        exit(0)

    operation = ""
    halted = False
    inputs = 0
    i = 0

    while not halted:
        if opcode[i] == 99:
            return -1

        operation = str(opcode[i])
        while len(operation) < 5:
            operation = "0" + operation

        # addition opcode, c = a + b
        if operation[3:] == "01":
            a,b = retrieve_param(opcode,operation,i+1,i+2)
            # print("Adding %d and %d and storing at %d" % (a,b,as_value(i+3)))
            opcode[as_value(opcode,i+3)] = a + b
            i+=4
        # addition opcode, c = a * b
        elif operation[3:] == "02":
            a,b = retrieve_param(opcode,operation,i+1,i+2)
            # print("Multiplying %d and %d and storing at %d" % (a,b,as_value(i+3)))
            opcode[as_value(opcode,i+3)] = a * b
            i+=4
        elif operation[3:] == "03":
            if inputs == 0:
                # print("Input Desired %d storing at %d" % (phase,as_value(i+1)))
                opcode[as_value(opcode,i+1)] = int(phase)
                inputs+=1
            elif inputs == 1:
                # print("Input Desired %d storing at %d" % (input_val,as_value(i+1)))
                opcode[as_value(opcode,i+1)] = int(input_val)
            else:
                print("Too Many Inputs")
                exit(1)
            i+=2
        elif operation[3:] == "04":
            a = retrieve_param(opcode,operation,i+1)
            # print("Output Desired %d" % a)
            return(a)
            i+=2
        elif operation[3:] == "05":
            a,b = retrieve_param(opcode,operation,i+1,i+2)
            # print("Jumping to %d if %d != 0" % (b,a))
            i = i+3 if a == 0 else b
        elif operation[3:] == "06":
            a,b = retrieve_param(opcode,operation,i+1,i+2)
            # print("Jumping to %d if %d == 0" % (b,a))
            i = b if a == 0 else i+3
        elif operation[3:] == "07":
            a,b = retrieve_param(opcode,operation,i+1,i+2)
            # print("%d < %d ? %d and storing at %d" % (a,b, a < b,as_value(i+3)))
            opcode[as_value(opcode,i+3)] = 1 if  a < b else 0
            i+=4
        elif operation[3:] == "08":
            # print("%d == %d ? %d and storing at %d" % (a,b, a == b,as_value(i+3)))
            a,b = retrieve_param(opcode,operation,i+1,i+2)
            opcode[as_value(opcode,i+3)] = 1 if  a == b else 0
            i+=4

"""
Desc:
Param: path: file path to pasword range
"""
def part_1(path):
    opcodes = read_file(path or PATH,return_type=int,strip=True,split=",")
    highest_output = 0
    best_phase = []

    for code in opcodes:
        for phase_setting in list(permutations([0,1,2,3,4])):
            prev_input = 0
            for phase in phase_setting:
                opcode = code.copy()
                prev_input = comput_opcode(opcode,phase,prev_input)
            if prev_input > highest_output:
                highest_output = prev_input
    print ( highest_output )


def part_2(path):
    opcodes = read_file(path or PATH,return_type=int,strip=True,split=",")
    highest_output = 0
    best_phase = []
    generation = 0

    for code in opcodes:
        for phase_setting in list(permutations([5,6,7,8,9])):
            prev_input = 0
            last_amplifier = 0
            opcode_phase = [code.copy(),code.copy(),code.copy(),code.copy(),code.copy()]

            while prev_input != -1:
                amplifier = generation % 5
                prev_input = comput_opcode(opcode_phase[amplifier],phase_setting[amplifier],prev_input)
                print(prev_input, generation)
                print(opcode_phase)
                input()
                # print(amplifier,prev_input,generation)
                if amplifier == 4:
                    last_amplifier = prev_input
                generation+=1
            # print(phase_setting, last_amplifier)
            if last_amplifier > highest_output:
                highest_output = last_amplifier
    # print ( highest_output )


if __name__ == '__main__':
    arguments(part_1,part_2)
    print("\n")
