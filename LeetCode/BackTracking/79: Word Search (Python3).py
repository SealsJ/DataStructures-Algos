class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Get Dimensions of the board
        ROWS, COLS = len(board) , len(board[0])

        #Make sure we don't revist letters in our path use Set
        path = set()

        #Create Nested dfs function (Need position in the board + i current character we are looking for)
        def dfs(r, c, i):
            if i == len(word):
                return True
            #If we go out of bounds or incorrect word, or visited same position twice
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False
            
            path.add((r,c))
            #Recursive call on all 4 adjacent positions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            #no longer have to visit position in path since we found solution
            path.remove((r,c))
            return res

        #Run through every position in the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        #Did not find solution (word) we were looking for
        return False
        
        #Time Complexity O(n * m * 4^n)
