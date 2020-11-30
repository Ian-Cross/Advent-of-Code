from reused import arguments, read_file

PATH="9thDay/input.txt"

class IntcodeComputer():
    def __init__(self,opcode):
        self.opcode = opcode
        self.relative_base = 0

    def as_index(self,val):
        opcode = self.opcode
        return opcode[opcode[val]];

    def as_value(self,val):
        opcode = self.opcode
        return opcode[val];

    def as_relative(self,val):
        opcode = self.opcode
        return opcode[self.relative_base + opcode[val]];

    def reference_mode(self,value,param_mode):
        if param_mode == "0":
            return self.as_index(value)
        elif param_mode == "1":
            return self.as_value(value)
        elif param_mode == "2":
            return self.as_relative(value)

    def retrieve_param(self,operation,a = None,b = None):
        print(operation,a,b)

        if a is not None and b is not None:
            print("Two Params")
            values = (self.reference_mode(a,operation[2]),
                      self.reference_mode(b,operation[1]))
        elif a is not None:
            print("One Param")
            values = self.reference_mode(a,operation[2])
        # elif c is None:
        #      values = self.reference_mode(a,operation[2])
        return values

    def compute_opcode(self):
        """
        Desc: Execute the opcode returning the computer list
        Param: opcode: list of ints used to simulate an Intcode computer,
        """
        opcode = self.opcode
        if not opcode:
            print("Please provide an opcode for computation")
            exit(0)

        operation = ""
        halted = False
        read_head = 0

        while not halted:
            try:
                if opcode[read_head] == 99:
                    halted = True

                operation = str(opcode[read_head])
                while len(operation) < 5:
                    operation = "0" + operation

                print(operation)

                if operation[3:] == "01":
                    a,b = self.retrieve_param(operation,read_head+1,read_head+2)
                    print("Adding: %s + %s = %d, storing at %d" % (a,b,a+b,self.as_value(read_head+3)))
                    opcode[self.retrieve_param(operation,read_head+3)] = a + b
                    read_head+=4
                elif operation[3:] == "02":
                    a,b = self.retrieve_param(operation,read_head+1,read_head+2)
                    print("Multiplying: %s * %s = %d, storing at %d" % (a,b,a*b,self.as_value(read_head+3)))
                    opcode[self.as_value(read_head+3)] = a * b
                    read_head+=4
                elif operation[3:] == "03":
                    print("Wanting Input: storing at %s" % self.retrieve_param(operation,read_head+1))

                    if operation[2] == "0":
                        opcode[opcode[read_head+1]] = int(input())
                    elif operation[2] == "1":
                        opcode[read_head+1] = int(input())
                    elif operation[2] == "2":
                        opcode[self.relative_base+opcode[read_head+1]] = int(input())
                    read_head+=2
                elif operation[3:] == "04":
                    a = self.retrieve_param(operation,read_head+1)
                    print("Diagnostic Test: %s" % (a))
                    read_head+=2
                elif operation[3:] == "05":
                    a,b = self.retrieve_param(operation,read_head+1,read_head+2)
                    print("Jumping: %s != 0 ? %s" % (a,b))
                    read_head = read_head+3 if a == 0 else b
                elif operation[3:] == "06":
                    a,b = self.retrieve_param(operation,read_head+1,read_head+2)
                    print("Jumping: %s == 0 ? %s" % (a,b))
                    read_head = b if a == 0 else read_head+3
                elif operation[3:] == "07":
                    a,b = self.retrieve_param(operation,read_head+1,read_head+2)
                    print("Less Than: %s < %s ? 1 : 0, storing at %d" % (a,b,self.as_value(read_head+3)))
                    opcode[self.as_value(read_head+3)] = 1 if  a < b else 0
                    read_head+=4
                elif operation[3:] == "08":
                    a,b = self.retrieve_param(operation,read_head+1,read_head+2)
                    print("Equal: %s == %s ? 1 : 0, storing at %d" % (a,b,self.as_value(read_head+3)))
                    opcode[self.as_value(read_head+3)] = 1 if  a == b else 0
                    read_head+=4
                elif operation[3:] == "09":
                    a = self.retrieve_param(operation,read_head+1)
                    print("Moving Base: opcode[%s+%s] = %a, %s + %s -> %s" % (self.relative_base,opcode[read_head+1],opcode[self.relative_base+opcode[read_head+1]],self.relative_base,a,self.relative_base+a))
                    self.relative_base += a
                    read_head+=2

                print(opcode)
                input()
            except IndexError:
                self.opcode.extend([0,0,0,0,0,0,0,0,0,0])


"""
Desc:
Param: path: filepath to the input data
"""
def part_1(path):
    opcodes = read_file(path or PATH,return_type=int,strip=True,split=",")

    for code in opcodes:
        computer = IntcodeComputer(code)
        computer.compute_opcode()


"""
Desc: Analize the layers, and build a final coloured image from combination of layers
Param: path: filepath to the input data
"""
def part_2(path):
    pass


if __name__ == '__main__':
    arguments(part_1,part_2)
    print()
