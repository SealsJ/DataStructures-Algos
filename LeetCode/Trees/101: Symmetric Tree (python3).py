# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #Create an empty queue, adding the first two children
        queue = deque([root.left, root.right])

        while queue:
            left = queue.popleft()
            right = queue.popleft()

            #If the left and right child are both empty, we just pass over since they are both null
            if not left and not right:
                continue

            #If one of the children are empty, means they aren't mirrors and we'd return False
            if not left or not right:
                return False

            #If the left value and right value of the children don't equal then they aren't mirrors, return False
            if left.val != right.val:
                return False

            #Key of the problem, how we add children to the queue, work our way from the outside towards the center for each level
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        #If passes all previous cases, then return True we have a mirror
        return True
