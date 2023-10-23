# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        #Initialize a queue for BFS Traversal, level by level comparision of x and y
        queue = deque([root])

        while queue:
            #Utilize a hashmap to store the parent/child relationship as we traverse the level
            parent = {}
            #For every level, we will see if x and y are on same level
            for i in range(len(queue)):
                curr = queue.popleft()
                #Append left and right child of current node to the queue
                for child in [curr.left, curr.right]:
                    if not child: continue
                    queue.append(child)
                    #Add child value to parent hashmap and set it equal to parent node
                    parent[child.val] = curr
            #If only x or only y are present in the level, they cant be cousins
            if (x in parent) ^ (y in parent): return False
            #If they are both in hahsmap and they don't have the same parent, then cousins
            if x in parent and y in parent:
                if parent[x] == parent[y]: return False
                else: return True
        #If we traversed entire tree and don't find x and y, just return False
        return False
