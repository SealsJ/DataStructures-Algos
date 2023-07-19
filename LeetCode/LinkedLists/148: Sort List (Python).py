# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        #if head is empty or head.next is empty, return head
        if not head or not head.next:
            return head

        p, slow, fast = None, head, head

        #p is a pointer used to split our list into two parts
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        p.next = None

        #Recursive call on merge function to sort two halves
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        #moving the pointers depending on which one has lower values
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        #Considering the case if one of the lists is empty
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        #So we don't return dummy variable, fake head node, and only return true head node
        return dummy.next
