# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Time Complexity: O(n) // Better than O(n^2) of making repeated parent child comparisons at every node down the entire BST

        #Create DFS Recursive function to explore left and right child
        def dfs(node, left, right):
            if not node:
                return True #Return true, no node is considered BST

            if not (node.val > left and node.val < right):
                return False #Return false, becuase criteria of BST has been invalidated

            #Root node has to be greater than all left children but less than all right children
            return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right)) #Recursive call on left and right child, both must return True

        return dfs(root, float("-inf"), float("inf"))
