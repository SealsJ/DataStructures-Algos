# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        previous, current = None, head
        #Time complexity O(n), Space Complexity O(1)
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous

    #Recursive Solution: T -> O(n) , S - > O(n)
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None
    
    return newHead
