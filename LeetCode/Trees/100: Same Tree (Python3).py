# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #DFS Recursive Traversal // TIME COMPLEXITY -> O(p + q)

        #BASE CASES
        #1) If both p and q are empty
        if not p and not q:
            return True
        #2) If one, p or q, is empty or not equal
        if not p or not q or p.val != q.val:
            return False

        #Recursive calls on left and right children
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
