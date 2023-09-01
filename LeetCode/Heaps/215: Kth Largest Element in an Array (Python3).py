class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
