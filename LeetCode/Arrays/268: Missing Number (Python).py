    def missingNumber(self, nums):
        #Gauss' Formuala Solution
        N = len(nums)

        expectedSum = (N * (N+1)) // 2
        actualSum = sum(nums)

        return expectedSum - actualSum
