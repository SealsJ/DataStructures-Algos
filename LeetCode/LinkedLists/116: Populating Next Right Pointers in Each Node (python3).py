"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #If root node is empty, return None
        if not root:
            return None

        #Keep track of the leftmost node for every level
        leftMost = root
        
        #We know this is Perfect Binary Tree, so if leftMost.left is None, then there are no leaves on that level and we can stop while loop
        while leftMost.left:
            curr = leftMost
            #while curr node isn't null, we are building the chains for the nodes beneath it in the tree
            while curr:
                #Bottom left node's next = right child of current node
                curr.left.next = curr.right
                #If curr.next, meaning there are more nodes on the current level, then we have to bridge middle children between them
                if curr.next:
                    #Current nodes right child has a next of the left child of the next node
                    curr.right.next = curr.next.left
                #Move current over to current next, which we created already in our traversal (basically root.left -> root.right)
                curr = curr.next
            #Update leftMost until left child is null, meaning we reached the last level of the tree and connected all children
            leftMost = leftMost.left

        return root

    #Utilizing a Linked List, in Space, gives us Constant Time Space Complexity compared to O(n) if we used a queue to solve this problem
