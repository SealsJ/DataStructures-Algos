class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Create an empty list to store all our unique combinations
        combos = []

        #Create the backtracking function (DFS of Decision Tree)
        def dfs(start_index, current_path, total):
            #Base case where we find a solution
            if total == target:
                #Append copy of current since we still want to use it in recursive calls
                combos.append(current_path[:])
                return
            #Base case where we go out of bounds or over the target value
            if start_index >= len(candidates) or total > target:
                return

            #First Decision where we decide to include duplicate values
            current_path.append(candidates[start_index])
            dfs(start_index, current_path, total + candidates[start_index])
            current_path.pop()

            #Second Decision where we branch and restrict duplicate choices
            dfs(start_index + 1, current_path, total)

        
        dfs(0, [], 0)
        return combos
