from heapq import heapify, heappush, heappop
from functools import total_ordering

## Python Tutor visualizer: https://pythontutor.com/render.html#code=class%20Node%3A%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.neighbors%20%3D%20%5B%5D%20%23%23%20List%20of%20Nodes%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f'Node%20%7Bself.value%7D%20has%20neighbors%20%7Bself.neighbors%7D'%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f'Node%3A%20%7Bself.value%7D'%0A%0A%0Aclass%20Graph%28%29%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.nodes%20%3D%20%5B%5D%0A%0A%20%20%20%20def%20add_node%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20Node%28value%29%0A%20%20%20%20%20%20%20%20self.nodes.append%28node%29%0A%0A%20%20%20%20def%20add_edge%28self,%20source_name,%20dest_name%29%3A%0A%20%20%20%20%20%20%20%20source_node,%20dest_node%20%3D%20None,%20None%0A%0A%20%20%20%20%20%20%20%20%23%23%20Find%20the%20target%20node%0A%20%20%20%20%20%20%20%20for%20node%20in%20self.nodes%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node.value%20%3D%3D%20dest_name%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20dest_node%20%3D%20node%0A%0A%20%20%20%20%20%20%20%23%23%20Find%20the%20source%20node%0A%20%20%20%20%20%20%20%20for%20node%20in%20self.nodes%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node.value%20%3D%3D%20source_name%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node.neighbors.append%28dest_node%29%0A%0A%20%20%20%20def%20print%28self%29%3A%0A%20%20%20%20%20%20%20%20for%20node%20in%20self.nodes%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28node%29%0A%0A%20%20%20%20def%20out_degree%28self,%20target%29%3A%0A%20%20%20%20%20%20%20%20for%20node%20in%20self.nodes%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node.value%20%3D%3D%20target%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20len%28node.neighbors%29%0A%0A%20%20%20%20def%20in_degree%28self,%20target%29%3A%0A%20%20%20%20%20%20%20%20num_in_edges%20%3D%200%0A%20%20%20%20%20%20%20%20for%20node%20in%20self.nodes%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20neighbor_name%20in%20node.neighbors%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20neighbor_name%20%3D%3D%20target%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20num_in_edges%20%2B%3D%201%0A%20%20%20%20%20%20%20%20return%20num_in_edges%0A%0A%0Aseattle%20%3D%20Graph%28%29%0Aseattle.add_node%28'green%20lake'%29%0Aseattle.add_node%28'uw'%29%0Aseattle.add_node%28'slu'%29%0Aseattle.add_node%28'cap%20hill'%29%0Aseattle.add_node%28'fremont'%29%0Aseattle.add_node%28'space%20needle'%29%0A%0Aseattle.add_edge%28'green%20lake',%20'uw'%29%0Aseattle.add_edge%28'green%20lake',%20'slu'%29%0Aseattle.add_edge%28'uw',%20'cap%20hill'%29%0Aseattle.add_edge%28'cap%20hill',%20'slu'%29%0Aseattle.add_edge%28'slu',%20'fremont'%29%0Aseattle.add_edge%28'fremont',%20'space%20needle'%29%0Aseattle.add_edge%28'fremont',%20'green%20lake'%29&cumulative=false&curInstr=284&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
## https://tinyurl.com/42buf82r

@total_ordering
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = [] ## List of Edges
        self.path_distance = 0
        self.visited = False

    def __str__(self):
        return f'Node {self.value} has neighbors {self.neighbors}'

    def __repr__(self):
        return f'Node: {self.value} [{self.path_distance}]'

    def __lt__(self, other):
        return self.path_distance < other.path_distance

class Edge:
    def __init__(self, node1, node2, distance):
        self.source = node1
        self.destination = node2
        self.distance = distance

class Graph():
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)

    def add_edge(self, source_name, dest_name, distance):
        source_node, dest_node = None, None

        ## Find the target node
        for node in self.nodes:
            if node.value == dest_name:
                dest_node = node

       ## Find the source node
        for node in self.nodes:
            if node.value == source_name:
                edge = Edge(node, dest_node, distance)
                node.neighbors.append(edge)

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


def djikstra(graph:Graph, source_name:str, target_name:str):
    visited = []
    nodes_to_visit = graph.nodes.copy() ## List of Nodes
    ## List of (name, path_distance)

    for node in nodes_to_visit:
        if node.value == source_name:
            node.path_distance = 0
        else:
            node.path_distance = 1000000

    heapify(nodes_to_visit) ## O(n)
    # nodes_to_visit.sort() ## O(n log n)

    while nodes_to_visit:
        node = nodes_to_visit.pop(0) ## O(n)
        # node = heappop(nodes_to_visit)  ## O(n)
        node.visited = True
        visited.append(node)
        ## Relax step
        for edge in node.neighbors:
            if not edge.destination.visited:
                edge.destination.path_distance = node.path_distance + edge.distance

        heapify(nodes_to_visit)

    print(visited)


seattle = Graph()
seattle.add_node('green lake')
seattle.add_node('uw')
seattle.add_node('slu')
seattle.add_node('cap hill')
seattle.add_node('fremont')
seattle.add_node('space needle')

seattle.add_edge('green lake', 'uw', 3)
seattle.add_edge('green lake', 'slu', 5)
seattle.add_edge('uw', 'cap hill', 7)
seattle.add_edge('cap hill', 'slu', 4)
seattle.add_edge('slu', 'fremont', 2)
seattle.add_edge('fremont', 'space needle', 8)
seattle.add_edge('fremont', 'green lake', 10)


djikstra(seattle, 'green lake', 'space needle')

play_graph = Graph()
play_graph.add_node('Start')
play_graph.add_node('A')
play_graph.add_node('B')
play_graph.add_node('Finish')
play_graph.add_edge('Start', 'A', 6)
play_graph.add_edge('Start', 'B', 2)
play_graph.add_edge('B', 'A', 3)
play_graph.add_edge('B', 'Finish', 5)
play_graph.add_edge('A', 'Finish', 1)


djikstra(play_graph, 'Start', 'Finish')