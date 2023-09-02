# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Empty list to return our level order traversal
        result = []

        #Take care of the edge case where the root is empty
        if root is None:
            return result
        
        #BFS can be implemented with a queue data structure
        queue = deque()
        queue.append(root)

        #while queue isn't empty, append to result layer by layer
        while queue:
            #appended to result list to create nested list 
            lvl_vals = []
            lvl_size = len(queue)

            for i in range(lvl_size):
                curr = queue.popleft()
                lvl_vals.append(curr.val)
            
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            result.append(lvl_vals)

        return result
