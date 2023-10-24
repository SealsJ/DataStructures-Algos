# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #TIME COMPLEXITY AND SPACE COMPLEXITY: O(n)
      
        #Create a global variable that we can access inside our helper dfs function
        #This will represent our max diamater
        res = [0]

        def dfs(root):
            #If null value, return -1 based on convention, makes math workout for finding height of nodes
            if not root:
                return -1

            #Recursively call on the left and right children of the root to find their heights
            left = dfs(root.left)
            right = dfs(root.right)
            #Update diamater value based on heights of left and right child
            res[0] = max(res[0], 2 + left + right)

            #return the diamater value running through the current node
            return (1 + max(left,right))
        
        dfs(root)
        return res[0]
