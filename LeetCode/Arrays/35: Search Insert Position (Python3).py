class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Binary Search Algo, TC: O(logn), SC: O(n)
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low
