# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #Base Case if root1 and root2 are both empty
        if not root1 and not root2:
            return None

        #Assign the value of each node to variable for addition, 0 is if its null (empty)
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        #Create a New Node for new Binary Tree to store sum value
        root = TreeNode(v1 + v2)

        #Recursive call on both left and right subtrees
        root.left = self.mergeTrees(root1.left if root1 else 0, root2.left if root2 else 0)
        root.right = self.mergeTrees(root1.right if root1 else 0, root2.right if root2 else 0)

        return root

        #TC is O(n + m) because we are traversing the length of each tree
