class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Python doesn't have max heap, use min heap to simulate it
        #Make list of stones negative to maintain max heap structure
        stones = [-s for s in stones]

        #Create max heap structure
        heapq.heapify(stones)

        #Pop two largest stones
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, first - second)

        #Edge case where there is no stones
        stones.append(0)

        return abs(stones[0])
