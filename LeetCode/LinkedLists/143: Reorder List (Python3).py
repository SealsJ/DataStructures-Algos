# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Two pointers, fast and slow, to find middle of linked list
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        #Reverse second half of linked list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #Merge two halves together
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
