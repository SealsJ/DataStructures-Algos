class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        uniqueJewels = set(jewels)
        count = 0

        for i in range(len(stones)):
            if stones[i] in uniqueJewels:
                count += 1
        return count
