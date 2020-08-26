from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list) # Graph representation : Adjacency List
        self.V = V
        # self.result = list()

    def add_edge(self, u, v):
        self.graph[u].append(v) # Directed Graph

    # def DFS(self, vertex):
    #     print("\n <-------- DFS --------> ")
    #     visited = [False] * (max(self.graph) + 1)  # n(vertices) = Highest Key of the dict + 1 (zero indexing)
    #     self._dfs_util(vertex, visited)

    def DFS_disconnected_graph(self):
        print("\n <-------- DFS --------> ")
        visited = [False] * (max(self.graph) + 1)  # n(vertices) = Highest Key of the dict + 1 (zero indexing)

        # If the graph has multiple connected components i.e. Disconnected Graph
        # Run DFS from all unvisited nodes after completion of the DFS call
        for vertex in range(self.V):
            if not visited[vertex]:
                self._dfs_util(vertex, visited)
        # print(self.result)

    def _dfs_util(self, node, visited):
        visited[node] = True
        print(node, end=" ")
        # self.result.append(node)

        for nb in self.graph[node]:
            if not visited[nb]:
                self._dfs_util(nb, visited)

    # def BFS(self, node):
    #     print("\n <-------- BFS --------> ")
    #     visited = [False] * (max(self.graph) + 1)
    #     self._bfs_util(node, visited)

    def BFS_disconnected_graph(self):
        print("\n <-------- BFS --------> ")
        visited = [False] * (self.V)
        for vertex in range(self.V):
            if not visited[vertex]:
                self._bfs_util(vertex, visited)

    def _bfs_util(self, node, visited):
        queue, visited[node] = [node], True
        while queue:
            curr_node = queue.pop(0)
            print(curr_node, end=" ")

            for nb in self.graph[curr_node]:
                if not visited[nb]:
                    queue.append(nb)
                    visited[nb] = True


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    # g.DFS(2)
    # g.BFS(2)

    dg = Graph(7)
    dg.add_edge(0, 1)
    dg.add_edge(1, 2)
    dg.add_edge(2, 0)
    dg.add_edge(0, 2)

    dg.add_edge(3, 4)
    dg.add_edge(4, 5)
    dg.add_edge(5, 4)
    dg.add_edge(4, 6)
    dg.add_edge(6, 6)

    dg.DFS_disconnected_graph()
    dg.BFS_disconnected_graph()
