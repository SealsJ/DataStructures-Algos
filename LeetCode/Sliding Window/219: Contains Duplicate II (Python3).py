class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Initialize a hashset to keep track of all values in window
        window = set()
        l = 0
        
        for r in range(len(nums)):
            #Maintain size of window
            if r - l > k:
                window.remove(nums[l])
                l += 1
            #Duplicate is present
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
