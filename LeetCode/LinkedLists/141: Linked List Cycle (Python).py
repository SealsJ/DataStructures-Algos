# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        #Start both pointers at the head node
        slowMarker, fastMarker = head, head

        #when fast marker reaches end first, if it equals null or the next node equals null then we know that there isn't a cycle in linked list
        while fastMarker != None and fastMarker.next != None:
            #Move the slowMarker one, move the fastMarker twice
            slowMarker = slowMarker.next
            fastMarker = fastMarker.next.next
            #if slowMarker ever equals the same node as the fastMarker then we know there was a cycle present
            if slowMarker == fastMarker:
                return True
        
        #no cycle in our linked list
        return False

#Linear time O(N), Constant space O(1)
