from reused import arguments, read_file
from collections import defaultdict, deque

PATH = "2025/day11/test.txt"


def calculate_indegree(network):
    """
    Calculate the number of incoming edges for each node in the network.
    """
    indegree = defaultdict(int)
    for node in network:
        for neighbor in network[node]:
            indegree[neighbor] += 1
        if node not in indegree:
            indegree[node] = indegree[node]  # ensure all nodes are present
    return indegree


def topological_sort(network):
    """
    Sort the nodes from top to bottom, pulling off nodes without incoming edges first and decreasing indegree of their neighbors.
    """
    indegree = calculate_indegree(network)
    queue = deque([node for node in indegree if indegree[node] == 0])
    topo = []
    while queue:
        node = queue.popleft()
        topo.append(node)
        for neighbor in network.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return topo


def count_paths_dag(network, start, end):
    topo = topological_sort(network)

    paths = {node: 0 for node in network}
    paths[end] = 1
    for node in reversed(topo):
        for neighbor in network.get(node, []):
            paths[node] += paths[neighbor]
    return paths[start]


def count_paths_dag_required(network, start, end, required_keys):

    # Create a bitmask for required keys
    key_to_idx = {k: i for i, k in enumerate(required_keys)}
    full_mask = (1 << len(required_keys)) - 1
    
    topo = topological_sort(network)

    paths = defaultdict(int)
    paths[(start, 0)] = 1

    for node in topo:
        for mask in [m for (n, m) in paths if n == node]:
            count = paths[(node, mask)]
            for neighbor in network.get(node, []):
                new_mask = mask
                if neighbor in key_to_idx:
                    new_mask |= 1 << key_to_idx[neighbor]
                paths[(neighbor, new_mask)] += count
    return paths[(end, full_mask)]


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    network = {}
    for line in file_data:
        key, paths = line.split(": ")
        network[key] = paths.split(" ")

    return count_paths_dag(network, "you", "out")


def part2(path):

    file_data = read_file(path or PATH, return_type=str, strip=True)
    network = {}
    for line in file_data:
        key, paths = line.split(": ")
        network[key] = paths.split(" ")

    return count_paths_dag_required(network, "svr", "out", ["dac", "fft"])


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
