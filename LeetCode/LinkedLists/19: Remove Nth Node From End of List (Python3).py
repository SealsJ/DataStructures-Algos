# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            #Initialize a dummy node to return head of list later
            dummy = ListNode(0, head)
            #Create two pointers to iterate through the list
            l = dummy
            r = head

            #Offset between two pointers is n, so node removed is always correct
            while n > 0 and r:
                r = r.next
                n -= 1

            while r:
                l = l.next
                r = r.next

            #Change left pointer to remove node
            l.next = l.next.next

            return dummy.next
