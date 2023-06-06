class Solution(object):
    def numIdenticalPairs(self, nums):
        #Need something to store the count of good pairs
        count = 0
        #Need a for loop to index through the array and find pairs
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
            #Conditions for a good pair
                if nums[i] == nums[j] and i < j:
                    count += 1

        return count
