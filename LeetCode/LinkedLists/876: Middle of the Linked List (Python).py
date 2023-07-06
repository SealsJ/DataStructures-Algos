# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        #store nodes to an array, then use the index to return value
        array = [head]
        #append values to array until you reach end of linked list
        while array[-1].next != None:
            array.append(array[-1].next)
        
        #return middle index, or second middle number if even
        return array[len(array) // 2]

        #Two Pointer Solution O(N)
        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
