# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        #Creating a dummy value to consider edgecases
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
