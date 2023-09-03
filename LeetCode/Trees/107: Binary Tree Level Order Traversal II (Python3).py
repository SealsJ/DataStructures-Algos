# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Make result a deque so we can append to the left hand side and give output in reverse order
        results = deque()

        if root is None:
            return results

        queue = deque()
        queue.append(root)

        while queue:
            level = []
            level_length = len(queue)

            for i in range(level_length):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            #We could also just leave results as a list, and reverse it with [::-1] or reversed()
            results.appendleft(level)

        return results
