# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []

        result = []
        stack = []
        current = root

        #while the current node and stack isn't empty
        while current or stack:
            #while current isn't empty
            while current:
                stack.append(current)
                current = current.left

            #Pop off top of the stack and append it to the results array
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
