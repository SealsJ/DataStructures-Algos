class Solution(object):
    def shuffle(self, nums, n):
        #Create an empty array to store the values of our list
        list = []

        #Loop through the nums index adding nums[i] then nums[i] + n
        for i in range(n):
            list.append(nums[i])
            list.append(nums[i + n])
        
        #return the list value
        return list
