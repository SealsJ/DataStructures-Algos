"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Create a hashmap to store all the nodes we've already visited
        oldToNew = {}

        #Create DFS ALGO to search the graph
        def dfs(node):
            #if node already visited, return the copy
            if node in oldToNew:
                return oldToNew[node]

            #If clone doesn't exist, we have to create a copy
            copy = Node(node.val)
            oldToNew[node] = copy
            #Iterate through neighbors to see if they've been visited yet
            #Append list of neighbors to copy Node we just created
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        #Call function / Consider edge case of no nodes
        return dfs(node) if node else None


        #Time Complexity: O(n) = O(Edges + Nodes)

        #BFS APPROACH
        visited = {}

        if not node:
            return node

        queue = deque([node])
        visited[node] = Node(node.val)

        while queue:
            n = queue.popleft()
            
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        
        return visited[node]
