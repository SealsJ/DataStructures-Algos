class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #BFS GRAPH ALGO TRAVERSAL: TIME COMPLEXITY -> O(M * N)

        #Consider the edge case if no grid
        if not grid:
            return 0

        #Figure out dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        #Implement a set to keep track of 'islands' (1s) already visited / count islands
        visit = set()
        islands = 0

        #Create BFS function to determine where an island stops
        def bfs(r,c):
            #Iterative approach, using a queue data structure for memory
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            #Keeping track of island size by using conditions
            while q:
                row, col = q.popleft()
                #possible directions
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                #iterate through directions
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    #Check if in bounds
                    if (r in range(rows) and c in range(cols) and
                    grid[r][c] == "1" and (r,c) not in visit):
                        #We have to now run bfs on this island (Add to queue)
                        q.append((r,c))
                        visit.add((r,c))

        #Need to traverse every row/column to keep track of 1s
        for r in range(rows):
            for c in range(cols):
                #Increment only if 1 hasn't been visited before
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands 


        #DFS SOLUTION
        if not grid:
            return 0

        visit = set()

        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or (r,c) in visit):
                return
                
            visit.add((r,c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c ) not in visit:
                    islands += 1
                    dfs(r,c)

        return islands
