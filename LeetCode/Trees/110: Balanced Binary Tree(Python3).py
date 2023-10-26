# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #TIME AND SPACE COMPLEXITY: O(n) // Only traverse each node once working from the bottom up

        #Create DFS Helper function, that returns two variables, boolean for balanced, integer for height
        def dfs(root):
            #Base case, an empty node would be balanced with a height of 0
            if not root:
                return [True, 0]

            #Recursively call on the left and right child of the tree
            left, right = dfs(root.left), dfs(root.right)

            #Balanced will return a boolean if every node in the tree up to that point in recursive call is balanced or not
            #We have to check left child, right child, and then if height-balanced 
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            #Return boolean, and calculate max height of current node
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
