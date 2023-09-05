class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Three sets to store the information of Queens position
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        #result returns our possible answers
        res = []

        #Create the board where "." represents an empty space nxn
        board = [["."] * n for i in range(n)]

        #Creating backtrack function takes in rows
        def backtrack(r):
            #if row == n we found solution
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            #if we didn't get solution, need to adjust valid positions
            for c in range(n):
                #checking for valid queen spots
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                #Update sets for this instance
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                #remove sets for the next instance
                col.remove(c)      
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        #Call function on first position
        backtrack(0)
        return res
