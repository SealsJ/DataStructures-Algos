# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    #DFS RECURSIVE SOLUTION // TIME COMPLEXITY -> O(S * T) S = Nodes in root , T = Nodes in Subroot

        #Consider Edge Cases
        if not t: return True #If subroot is empty, it will be a subRoot
        if not s: return False #If root is empty, subroot can't exist

        if self.sameTree(s, t):
            return True

        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))


    #Define helper function to see if two trees are the same
    def sameTree(self, s, t):
        #If both trees are empty, they are the same
        if not s and not t:
            return True
        #if they have an equal value, return response of traversing left/right children
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))

        #If one of the trees is empty while the other isnt
        return False
