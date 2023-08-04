class Solution(object):
    def isValidSudoku(self, board):
        #Initializng a hashmap where key is the column # and value is a set represeting all values in the column 
        #Repeat with rows, this is to detect duplicates 
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r/3 , c/3)

        for r in range(9):
            for c in range(9):
                #If empty, we just continue and ignore
                if board[r][c] == ".":
                    continue
                #If value is already been seen in the current row/colum/square, means duplicate is present
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
            #Updating our hashset to reflect the new rows/columns/squares in our current sudoku board
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
