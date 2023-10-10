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


        #Second Answer in O(n) TC
        class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            length = len(nums)
            products = [1] * length
            for i in range(1, length):
                products[i] = products[i-1] * nums[i-1]
    
            right = nums[-1]
            for i in range(length-2, -1, -1):
                products[i] *= right
                right *= nums[i]
            
            return products
