from reused import arguments, read_file

centre_of_mass = None
PATH="6thDay/input.txt"

"""
Desc: A tree node used to represent and object in an orbit
Param: name: a string value that contains the identifyer for that node in orbit
       parent: a reference to a OrbitNode that is the direct precessor to this OrbitNode in the tree
       child_nodes: a list of OrbitNodes that are the direct processor to this OrbitNode in the tree
"""
class OrbitNode:
    def __init__(self,name,parent):
        self.value = name
        self.child_nodes = []
        self.parent_node = parent

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    """
    Desc: Adding a child node onto the current node
    Param: child: a OrbitNode representing the child
    """
    def add_child(self,child):
        self.child_nodes.append(child)


"""
Desc: A redimentary recursive depth first search of the tree looking for a matching OrbitNode value
Param: node: The current OrbitNode, based on the position in the tree
       value: a string value of the identifyer for the OrbitNode desired
"""
def find_node(node,value):
    if node.value == value:
        return node
    for child in node.child_nodes:
        retreived_node = find_node(child, value)
        if retreived_node is not None:
            return retreived_node

"""
Desc: Builds a tree representation of OrbitNodes with centre_of_mass as the root
Param: orbit_pair: a list of size 2, containing identifyers for the center object and the orbit object
"""
def make_tree(orbit_pair):
    global centre_of_mass
    com = orbit_pair[0]
    obj = orbit_pair[1]

    # Due to the randomness of the input file,
    # ensure that there is at least a root node to add to
    if centre_of_mass is None and com != "COM":
        return False

    # Create the root node of the tree
    if com == "COM":
        centre_of_mass = OrbitNode(com,None)
        centre_of_mass.add_child(OrbitNode(obj,centre_of_mass))
        return True
    # Again, due to the randomness of the file the current orbit,
    # pair may not be able to be added yet.
    else:
        # find a node in the tree matching the center object
        # add the orbit object to the found node if found.
        node = find_node(centre_of_mass,com)
        if node is None:
            return False
        else:
            node.add_child(OrbitNode(obj,node))
            return True


count = 0
"""
Desc: Do a full recursive depth first tree transversal counting all the direct and indirect orbits of each OrbitNode
Param: node: the current OrbitNode, based on the position in the tree
       depth: int, current distance from the center_of_mass (root node)
"""
def count_tree(node,depth):
    global count
    count+=depth
    depth+=1
    for child in node.child_nodes:
        count_tree(child,depth)

"""
Desc: Build a tree representation of the input data, find how many direct and indirect orbits each OrbitNode has
Param: path: filepath to the input data
"""
def part_1(path):
    global centre_of_mass,count
    orbits = read_file(path or PATH, return_type=str,strip=True, split=")")

    # Due to the randomness of the data, iterate through
    # each pair searching for a node that fits into the tree,
    # then remove that pair from the data. Quit when all nodes
    # have been added to the tree
    while len(orbits) > 0:
        for i in range(len(orbits)):
            if make_tree(orbits[i]):
                orbits.remove(orbits[i])
                break

    # Tranvserse and count all orbits
    count_tree(centre_of_mass,0)

    print("The number of direct and indirect orbits in the data is: %d" % count)

"""
Desc: Recursively search the tree for a matching OrbitNode, once found, build a pathway back to the root OrbitNode
Param: node: the current OrbitNode, based on position in the tree
       value: a string value of the identifyer of the OrbitNode being searched for
"""
def find_node_trail(node,value):
    node = find_node(node,value)
    trail = [node]
    while node.parent_node is not None:
        node = node.parent_node
        trail.append(node)
    return trail

"""
Desc: Build a tree representation of the input data, and find the smallest pathway between two leaf nodes
Param: path: filepath to the input data
"""
def part_2(path):
    global centre_of_mass,count
    orbits = read_file(path or PATH, return_type=str,strip=True, split=")")

    # Due to the randomness of the data, iterate through
    # each pair searching for a node that fits into the tree,
    # then remove that pair from the data. Quit when all nodes
    # have been added to the tree
    while len(orbits) > 0:
        for i in range(len(orbits)):
            if make_tree(orbits[i]):
                orbits.remove(orbits[i])
                break

    # Find the pathways to two leaf nodes
    you_path = find_node_trail(centre_of_mass,"YOU")
    san_path = find_node_trail(centre_of_mass,"SAN")
    # print(you_path)
    # print(san_path)

    # Find a the first matching OrbitNode between the two leaf node pathways
    for node in you_path:
        if node in san_path:
            distance = san_path.index(node)-1 + you_path.index(node)-1
            break

    print("The minimum number of orbital transfers required between YOU and SAN is %d" % distance)

if __name__ == '__main__':
    arguments(part_1,part_2)
    print("\n")
