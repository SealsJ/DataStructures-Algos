# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Create empty list to return the result of the zigzag pattern
        result = []

        #Consider the edge case where root is empty, just return nothing
        if root is None:
            return result

        #BFS, use a deque for a queue data structure
        queue = deque()
        queue.append(root)
        #height variable is used as an indicator for which direction to append values to queue
        height = 1

        while queue:
            level_values = []
            level_length = len(queue)

            #if odd level, we add to queue as normal
            if height % 2 != 0:
                for i in range(level_length):
                    curr = queue.popleft()
                    level_values.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)

                    if curr.right:
                        queue.append(curr.right)

            #if even level, we need to add to queue in reverse order
            elif height % 2 == 0:
                 for i in range(level_length):
                    #pop the value from the end of the queue
                    curr = queue.pop()
                    level_values.append(curr.val)

                    #add values to the front of queue with right first to add to result in normal order
                    if curr.right:
                        queue.appendleft(curr.right)

                    if curr.left:
                        queue.appendleft(curr.left)

            #Append to result and adjust height of binary tree counter
            result.append(level_values)
            height += 1

        return result
