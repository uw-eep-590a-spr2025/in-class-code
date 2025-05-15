
## List of nodes: []
## Each node has a name/value, list of neighbors
## https://tinyurl.com/4z8hcvh7

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = [] ## List of strings, of the name of the neighbor

    def __str__(self):
        return f'Node {self.value} has neighbors {self.neighbors}'


class Graph():
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)

    def add_edge(self, source_name, dest_name):
        for node in self.nodes:
            if node.value == source_name:
                node.neighbors.append(dest_name)

    def print(self):
        for node in self.nodes:
            print(node)

    def out_degree(self, target):
        for node in self.nodes:
            if node.value == target:
                return len(node.neighbors)

    def in_degree(self, target):
        num_in_edges = 0
        for node in self.nodes:
            for neighbor_name in node.neighbors:
                if neighbor_name == target:
                    num_in_edges += 1
        return num_in_edges


seattle = Graph()
seattle.add_node('green lake')
seattle.add_node('uw')
seattle.add_node('slu')
seattle.add_node('cap hill')
seattle.add_node('fremont')
seattle.add_node('space needle')

seattle.add_edge('green lake', 'uw')
seattle.add_edge('green lake', 'slu')
seattle.add_edge('uw', 'cap hill')
seattle.add_edge('cap hill', 'slu')
seattle.add_edge('slu', 'fremont')
seattle.add_edge('fremont', 'space needle')
seattle.add_edge('fremont', 'green lake')


seattle.print()


print(seattle.out_degree('slu'))
print(seattle.in_degree('slu'))
