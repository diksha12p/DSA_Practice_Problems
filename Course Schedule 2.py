"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to
finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.

Example 1:
Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .


Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
"""
from typing import List


class Solution:
    def __init__(self):
        self.stack = []

    # IDEA 1: DFS -> Cycle Detection + TopSort Order generation
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adj_list = [[] for _ in range(numCourses)]
        for entry in prerequisites:
            self.adj_list[entry[1]].append(entry[0])

        # 0: Unvisited, 1: Currently visiting : on the recursion call stack, 2: Done processing
        self.visited = [0] * numCourses
        for course in range(numCourses):
            if not self.visited[course] and self._dfs(course): # Cycle Found
                return []
        return self.stack[::-1]

    def _dfs(self, node):
        self.visited[node] = 1
        for nb in self.adj_list[node]:
            if self.visited[nb] == 1: # Revisiting a node currently being processed -> Cycle exists
                return True
            if not self.visited[nb] and self._dfs(nb): # Cycle Found
                return True
        self.stack.append(node)
        self.visited[node] = 2 # Done processing the node

class SolutionAlt:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for pos, nb in prerequisites:
            adj_list[pos].append(nb)

        # Compute the in degree for each node
        in_degree = [0] * n
        for i in range(n):
            for j in adj_list[i]:
                in_degree[j] += 1

        # Initialize queue with all nodes having 0 in-degree
        queue, top_order = [], []
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        # Reduce in-degree for all the neighbors
        count = 0  # Tracks number of nodes visited
        while queue:
            node = queue.pop()
            top_order.append(node)

            count += 1
            for nb in adj_list[node]:
                in_degree[nb] -= 1
                # Add neighbor to queue if in-degree becomes 0
                if in_degree[nb] == 0:
                    queue.append(nb)

        # Check if n(nodes visited) == n(nodes) and return top sort answer accordingly
        return top_order[::-1] if count == n else []


if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(2, [[1, 0],[0, 1]]))
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

    sol_alt = SolutionAlt()
    print(sol_alt.findOrder(2, [[1, 0], [0, 1]]))
    print(sol_alt.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


