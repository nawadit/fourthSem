from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            current = queue.pop(0)
            if current not in visited:
                result.append(current)
                visited.add(current)
                queue.extend(self.graph[current])

        return result

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        result = []

        if start not in visited:
            result.append(start)
            visited.add(start)
            for neighbor in self.graph[start]:
                result.extend(self.dfs(neighbor, visited))

        return result

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    start_node = 0

    print("BFS traversal starting from node", start_node, ":", graph.bfs(start_node))
    print("DFS traversal starting from node", start_node, ":", graph.dfs(start_node))
