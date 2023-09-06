class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #Sort the input of nums
        nums.sort()

        #Perform a sliding window so need to initialize left and right pointer
        l, r = 0, 0

        #Result stores max frequency to return, total = total sum of current window
        res, total = 0, 0

        while r < len(nums):
            total += nums[r]

            #While the window is invalid, we have to shrink the window
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
            r += 1

        return res #Time Complexity O(nlogn)
