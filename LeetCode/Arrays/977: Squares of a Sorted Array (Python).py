class Solution(object):
    def sortedSquares(self, nums):
        #Creating an empty array to store the squared values
        squared = []

        #iterate through each value squaring the result
        for i in nums:
            squared.append(i * i)
        
                #return the sorted array O(nlogn)
        return sorted(squared)


        #Optimal Solution O(N): Two Pointers
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1

            result[i] = square * square
        return result
