class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        goodPairs = 0

        for i in nums:
            if i in hashmap:
                goodPairs += hashmap[i]
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        return goodPairs
