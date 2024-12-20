"""
Desc: Convert the type of the provided line, strips whitespace if chosen
Param: return_type: funtion pointer to the desired casting type for the output
       strip: boolean, to trim each line of whitespace
"""
import re

def convertType(line, return_type, strip):
    if strip:
        line = line.strip()
    return return_type(line)


"""
Desc: Convert the str line into a usable output defined by the parameters
Param: line: str, the input to be formated
       return_type: funtion pointer to the desired casting type for the output
       strip: boolean, to trim each line of whitespace
       split: str, a delimiter to use on each line for further separation of lines
       exclude_none: boolean, to exclude None values in the split output
"""


def format(line, return_type, strip, split, exclude_none):
    broken_line = None
    if split:
        broken_line = None
        if exclude_none:
            broken_line = list(filter(None,re.split(split,line)))
        else:
            broken_line = re.split(split, line)
        for i in range(len(broken_line)):
            broken_line[i] = convertType(broken_line[i], return_type, strip)
    else:
        broken_line = convertType(line, return_type, strip)
    return broken_line


"""
Desc: Read the provied datafile line by line and return the formatted output as a list
Param: path: file path to the datafile
       return_type: funtion pointer to the desired casting type for the output
       strip: boolean, to trim each line of whitespace
       split: str, a delimiter to use on each line for further separation of lines
       as_one: boolean, to return the entire file as a single string
       exclude_none: boolean, to exclude None values in the split output
"""


def read_file(path=None, return_type=str, strip=False, split=None, as_one=None, exclude_none=False):
    # Exit if no datafile is provided
    if not path:
        print("Please supply a path to the input file")
        exit(1)

    contents = []

    with open(path) as file:
        if as_one == True:
            contents = format("".join(file.readlines()),return_type,strip,split, exclude_none)
        else:
            for line in file:
                # Add the formatted line to the main list
                contents.append(format(line, return_type, strip, split, exclude_none))

    return contents
