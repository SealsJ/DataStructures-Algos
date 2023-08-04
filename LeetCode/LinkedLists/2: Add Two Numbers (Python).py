# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #Initialize empty LL to insert l1 / l2 to avoid edgecases
        dummy = ListNode()
        #Current pointer is set at the heady of dummy LL
        current = dummy
        #Establish carry value we have to maintain
        carry = 0

        #Iterate while either l1 or l2 has a digit
        while l1 or l2 or carry:
            #If l1 has a value, otherwise 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #Create new digit
            val = v1 + v2 + carry
            #Make new node for carry if two digit number (15)
            carry = val // 10
            #Update value to be ones place number
            val = val % 10
            #Add to new Linked List
            current.next = ListNode(val)

            #Update Pointer
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
