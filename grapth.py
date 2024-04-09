import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        """connect 2 vertices with same weight"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start, end):
        """find shortest path between two vertices"""
        distances = [float("inf")] * self.V # init all verrices distance from start as infinite
        distances[start] = 0
        priority_queue = [(0, start)]
        previous = [None] * self.V

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex == end:
                break  # Stop algorithm when the end node is reached

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor)) # add shortest path found to heap

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()  # Reverse to get the path from start to end

        return distances[end], path


# Example usage
if __name__ == "__main__":
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

if __name__ == "__main__":
    g = Graph(9)
    edges = [
        (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2),
        (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
        (6, 8, 6), (7, 8, 7)
    ]
    for (u, v, w) in edges:
        g.add_edge(u, v, w)

    start, end = 0, 4
    distance, path = g.dijkstra(start, end)
    print(f"Shortest path from {start} to {end} is {path} with distance {distance}")