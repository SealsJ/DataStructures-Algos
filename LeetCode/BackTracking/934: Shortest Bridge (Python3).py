class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #Check dimensions of the grid, NxN
        N = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        #Helper function to check if coordinates are invalid
        def invalid(r,c):
            return r < 0 or c < 0 or r == N or c == N

        #Have to brute force scan the grid to find first island and store coordinates
        visit = set()
        def dfs(r,c):
            #If not out of bounds, not water (0), or not stored in hashset
            if (invalid(r,c) or not grid[r][c] or (r,c) in visit):
                return 
            #This means its a 1, add coordinates to the set and check directions
            visit.add((r,c))
            #Calls DFS on all surrounding locations
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        #Now perform BFS to find shortest path between two islands
        #BFS doesn't need paramters, will use visit set for queue
        def bfs():
            result = 0 #Counter variable for shortest path
            queue = deque(visit)

            while queue:
                #Iterate through snapshot of each BFS Layer to keep track of path variables
                length = len(queue)
                for i in range(length):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return result
                        queue.append([curR, curC])
                        visit.add((curR, curC))
                result += 1


        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()
