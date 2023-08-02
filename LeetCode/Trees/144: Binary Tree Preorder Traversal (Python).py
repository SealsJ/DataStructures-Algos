# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        #Iterative
        res = []
        stack = [root]

        while stack:
            current = stack.pop()
            if current:
                res.append(current.val)
                stack.append(root.right)
                stack.append(root.left)

        return res

        #Recursive
        def dfs(node):
            if not node:
                return []
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return res
