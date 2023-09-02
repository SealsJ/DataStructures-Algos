# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #Creat an empty list to return the result
        result = []

        #Consider the edge case where the root is empty and we can return None
        if root is None:
            return result

        #BFS problem so we have to implement a queue data structure with deque()
        queue = deque()
        queue.append(root)

        while queue:
            #Calculate avg for each level then append that to result list for answer
            level_sum = 0
            level_size = len(queue)

            for i in range(level_size):
                curr = queue.popleft()
                level_sum += curr.val

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            #Once for loop is finished, calculate average for that level then add
            avg = level_sum / level_size
            result.append(avg)

        return result
