# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        #Array Solution, (Requires extra memory O(n))
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True
      
        #Do it in O(1) Memory, Two Pointer Solution
        slow, fast = head, head

        #Finding the middle of the linked list = slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half of linked list
        previous = None
        while slow:
            tmp = slow.next
            slow.next = previous
            previous = slow
            slow = tmp

        #Check if palindrome
        left, right = head, previous
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
