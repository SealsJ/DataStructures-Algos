class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Find the dimensions of the board
        rows, cols = len(board), len(board[0])
        path = set() #We want a way to track if we've seen a combination before (r,c)

        def dfs(r, c, i):
            if i == len(word): return True #Means we found the correct word

            #Now need to consider conditions where we have the wrong word
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or   #r,c is outside of defined board dimensions
                board[r][c] != word[i] or   #we have the wrong letter
                (r,c) in path):             #we've already seen this letter before in our path, can't reuse it
                return False

            #If we don't get false, means we have a letter that is apart of our word
            path.add((r,c))
            
            #Now we will recurisvely check all 4 directions to see if we can find the next letter in the word
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            path.remove((r,c)) #We hit dead end or answer in path, remove path and try a different direction
            return res #If any call returns true, that means we have found the word!


        #Now we call function for every combination of the board
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): #0 for starting index of the word, we found match return True
                    return True

        return False #We couldn't find a match so word doesn't exist


        #Time Complexity: O(n * m * 4^n) where n/m represent dimensions of the board and 4^n represents 4 dfs calls based on length of the word(n)
