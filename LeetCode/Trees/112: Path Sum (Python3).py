# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #DFS TRAVERSAL Recursive

        #Check if tree is empty
        if root is None:
            return False
        
        #Check if root node already equals target, and no children (1 node)
        if root.val == targetSum and root.left is None and root.right is None:
            return True

        #Recursive calling left/right children, subtracting value of previous node on the path
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
      
