class Solution(object):
    def minSubArrayLen(self, target, nums):
        window_start = 0
        min_len = len(nums) + 1 #invalid value always going to be larger : float(inf)
        current_sum = 0

        for window_end in range(len(nums)):
            current_sum += nums[window_end]
            while current_sum >= target:
                min_len = min(min_len, window_end - window_start + 1)
                current_sum -= nums[window_start]
                window_start += 1

        return 0 if min_len == len(nums) + 1 else min_len
