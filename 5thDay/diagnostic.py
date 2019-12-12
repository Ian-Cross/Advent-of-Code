from reused import arguments, read_file

PATH="5thDay/input.txt"
opcode = None

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
Desc: Extended Intcode computer with opcodes 3 & 4, for input and output
Param: path: file path to pasword range
"""
def part_1(path):
    global opcode
    opcodes = read_file(path or PATH,return_type=int,strip=True,split=",")

    """
    Desc: Execute the opcode returning the computer list
    Param: opcode: list of ints used to simulate an Intcode computer,
    """
    def comput_opcode():
        global opcode
        if not opcode:
            print("Please provide an opcode for computation")
            exit(0)

        operation = ""
        halted = False
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
                opcode[as_value(i+1)] = int(input())
                i+=2
            elif operation[3:] == "04":
                a = retrieve_param(operation,i+1)
                print("Diagnostic Test: %s " % a)
                i+=2

    for code in opcodes:
        opcode = code
        comput_opcode()

"""
Desc: Extended Intcode computer with opcodes 5, 6, 7, & 8, for jumping and comparrisons
Param: path: file path to pasword range
"""
def part_2(path):
    global opcode
    opcodes = read_file(path or PATH,return_type=int,strip=True,split=",")

    """
    Desc: Execute the opcode returning the computer list
    Param: opcode: list of ints used to simulate an Intcode computer,
    """
    def comput_opcode():
        global opcode
        if not opcode:
            print("Please provide an opcode for computation")
            exit(0)

        operation = ""
        halted = False
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
                opcode[as_value(i+1)] = int(input())
                i+=2
            elif operation[3:] == "04":
                a = retrieve_param(operation,i+1)
                print("Diagnostic Test: %s " % a)
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
        opcode = code
        comput_opcode()



if __name__ == '__main__':
    arguments(part_1,part_2)
    print("\n")
