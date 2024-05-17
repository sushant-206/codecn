class NetworkRouting:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, source, destination):
        visited = set()
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        predecessors = {}
        while len(visited) < len(self.graph):
            current_node = None
            min_distance = float('inf')
            for node in self.graph:
                if distances[node] < min_distance and node not in visited:
                    min_distance = distances[node]
                    current_node = node
            visited.add(current_node)
            for neighbor, weight in self.graph[current_node].items():
                if distances[current_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current_node] + weight
                    predecessors[neighbor] = current_node
        path = []
        current_node = destination
        while current_node != source:
            path.insert(0, current_node)
            current_node = predecessors[current_node]
        path.insert(0, source)
        return path

class AODV(NetworkRouting):
    def __init__(self, graph):
        super().__init__(graph)
        self.route_table = {}  # route table for AODV

    def discover_route(self, source, destination):
        # AODV Route Discovery
        if source not in self.route_table:
            self.route_table[source] = {}
        if destination not in self.route_table[source]:
            shortest_path = self.shortest_path(source, destination)
            if shortest_path:
                self.route_table[source][destination] = shortest_path
            else:
                return None
        return self.route_table[source][destination]

# Example usage
if __name__ == "__main__":
    # Creating a sample network graph
    graph = {
        "A": {"B": 1, "C": 2},
        "B": {"A": 1, "C": 1, "D": 3},
        "C": {"A": 2, "B": 1, "D": 1, "E": 4},
        "D": {"B": 3, "C": 1, "E": 1},
        "E": {"C": 4, "D": 1}
    }

    # Initialize routing protocols
    shortest_path_routing = NetworkRouting(graph)
    aodv_routing = AODV(graph)

    # Example usage of shortest path routing
    print("Shortest path from A to E:", shortest_path_routing.shortest_path("A", "E"))

    # Example usage of AODV routing
    print("Route discovered by AODV from A to E:", aodv_routing.discover_route("A", "E"))
