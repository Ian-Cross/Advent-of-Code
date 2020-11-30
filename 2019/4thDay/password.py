from reused import arguments, read_file

PATH="4thDay/input.txt"

"""
Desc: Checks the password to ensure it passes all checks:
        1. The nth char is never greater than the n+1th char
        2. Password contains a pair of identical chars
        3. If strick_double, password must contain at least 1 set of identical chars of size 2
Param: password: string, representing the current guess
       strick_double: boolean, useds as a flag to toggle between two opperating modes
"""
def check_password(password, strick_double = False):
    is_increse = True
    last_c = '0'
    matched = []
    matched_groups = []
    # Iterate throught the password 1 char at a time
    for c in password:
        # quit the loop if it is found to be decreasing
        if c < last_c:
            is_increse = False
            break
        if c == last_c:
            if strick_double:
                # If a pair has been found, identify the group
                if c not in matched:
                    matched_groups.append(True)
                # If the group has been identified already, mark it as to large
                else:
                    matched_groups.append(False)
            # Record the matched charater
            matched.append(c)
        else:
            matched_groups.append(None)
        last_c = c
    # Add on a padder
    matched_groups.append(None)

    if is_increse:
        # strick, check for a group that didn't get too large
        if strick_double:
            for i in range(len(matched_groups)-1):
                if matched_groups[i] == True and matched_groups[i+1] == None:
                    return password
        # non strick, as long as there has been 1 match it is valid
        elif len(matched) > 0:
            return password


"""
Desc: Cycle through the provided password range looking for non strick matches
Param: path: file path to pasword range
"""
def part_1(path):
    password_ranges = read_file(path or PATH,return_type=int,strip=True,split="-")

    for password_range in password_ranges:
        passwords = []
        for x in range(password_range[0],password_range[1]):
            passwords.append(check_password(str(x),strick_double=False))
        passwords = [password for password in passwords if password]
        print("There are %d passwords within the range %d - %d " % (len(passwords),password_range[0],password_range[1]))


"""
Desc: Cycle through the provided password range looking for strick matches
Param: path: file path to pasword range
"""
def part_2(path):
    password_ranges = read_file(path or PATH,return_type=int,strip=True,split="-")

    for password_range in password_ranges:
        passwords = []
        for x in range(password_range[0],password_range[1]):
            passwords.append(check_password(str(x),strick_double=True))
        passwords = [password for password in passwords if password]
        print("There are %d passwords within the range %d - %d " % (len(passwords),password_range[0],password_range[1]))



if __name__ == '__main__':
    arguments(part_1,part_2)
    print("\n")
