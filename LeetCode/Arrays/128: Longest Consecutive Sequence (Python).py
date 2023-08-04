class Solution(object):
    def longestConsecutive(self, nums):
      #initialize an empty set and tracker of longest sequence
        numSet = set(nums)
        longest = 0

        for i in nums:
            #Check if start of the sequence, does it not have left neighbor?
            if (i - 1) not in numSet:
                #check if each consecutive number exists in numSet to expand length
                length = 0
                while (i + length) in numSet:
                    length += 1
                #Compute longest length, compare it to previous sequnce lengths
                longest = max(length, longest)
        return longest
