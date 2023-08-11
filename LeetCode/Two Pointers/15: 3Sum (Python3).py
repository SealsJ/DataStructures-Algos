class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Create an empty array to store tuples, key is to sort the nums input!
        res = []
        nums.sort()

        #Enumerate to check the index plus its value! Don't want to use duplicates so continute if nums[i] == nums[i - 1]
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

          #Basically two sum problem now!
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    #Same as i pointer, don't want to use same l values so continute if same value
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
