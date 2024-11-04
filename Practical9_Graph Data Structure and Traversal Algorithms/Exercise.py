from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

    def shortest_path_bfs(self, start_vertex, end_vertex):
        visited = {start_vertex: None}
        queue = deque([start_vertex])

        while queue:
            vertex = queue.popleft()
            if vertex == end_vertex:
                break
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited[neighbor] = vertex
                    queue.append(neighbor)

        path = []
        while end_vertex is not None:
            path.append(end_vertex)
            end_vertex = visited[end_vertex]
        return path[::-1]  

    def has_cycle(self):
        visited = set()

        def _has_cycle(vertex, parent):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if _has_cycle(neighbor, vertex):
                        return True
                elif parent is not neighbor:
                    return True
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if _has_cycle(vertex, None):
                    return True
        return False

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.graph[current_vertex]:
                distance = current_distance + 1  
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def is_bipartite(self):
        color = {}
        
        for vertex in self.graph:
            if vertex not in color:
                color[vertex] = 0
                queue = deque([vertex])
                while queue:
                    current = queue.popleft()
                    for neighbor in self.graph[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False
        return True

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("\nShortest path from vertex 0 to vertex 3:")
print(g.shortest_path_bfs(0, 3))

print("\nDoes the graph have a cycle?", g.has_cycle())

print("\nDijkstra's algorithm (shortest paths from vertex 0):")
print(g.dijkstra(0))

print("\nIs the graph bipartite?", g.is_bipartite())


