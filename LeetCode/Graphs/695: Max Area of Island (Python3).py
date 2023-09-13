class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Create hashset to store coords already visited
        visited = set()

        #Determine dimensions of the graph
        rows, cols = len(grid), len(grid[0])

        #dfs: Check if coordinates are in range and not water
        def dfs(r,c):
            if (r not in range(rows) 
            or c not in range(cols) 
            or grid[r][c] != 1 
            or (r,c) in visited):
                return 0

            #Add coordinate to hashset so its not counted twice in area calculation
            visited.add((r,c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        #Area variable created to return
        area = 0
        #Double for loop to iterate through every combination in the board and find islands
        for r in range(rows):
            for c in range(cols):
                #return max of old island or current island
                area = max(area, dfs(r,c))

        return area

    #Time Complexity: O(M * N) -> Where worst case we go through entire board (M = rows / N = cols)
