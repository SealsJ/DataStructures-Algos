class Solution(object):
    def productExceptSelf(self, nums):
        #give result array which doesn’t interfere with memory constraint
        result = [1] * (len(nums))

        #iterate through original array getting ‘prefix’ product before i
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        #iterate through original array getting ‘postfix’ product after i
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
