class Graph:

    def __init__(self):
        self.graph = []

    def add_node(self, value):
        vertex = Vertex(value)
        if vertex not in self.graph:
            self.graph.append(vertex)
        return vertex

    def add_edge(self, v1, v2, wt=1):
        if v1 in self.graph and v2 in self.graph:
            edge = Edge(v2, wt)
            v1.adjacent_list.append([v2, edge])
        else:
            raise KeyError

    def get_nodes(self):
        return self.graph

    def get_neighbors(self, vertex):
        neighbors = []
        for item in self.graph:
            if item.value == vertex.value:
                for edges in item.adjacent_list:
                    neighbors.append(edges[1])
        return neighbors

    def size(self):
        return len(self.graph)


class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_list = []


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

if __name__ == '__main__':
    g = Graph()
    one = g.add_node("one")







