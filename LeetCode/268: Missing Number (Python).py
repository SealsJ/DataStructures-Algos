    def missingNumber(self, nums):
        N = len(nums)

        expectedSum = (N * (N+1)) // 2
        actualSum = sum(nums)

        return expectedSum - actualSum
