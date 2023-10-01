class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        mapping = {}
        res = []

        for i in range(len(temp)):
            if temp[i] not in mapping:
                    mapping[temp[i]] = i
        
        for i in range(len(nums)):
            res.append(mapping[nums[i]])
        return res
