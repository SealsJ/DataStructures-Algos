class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        #Create two instance variables for the inputs
        self.minHeap, self.k = nums, k
        #Utilizie a heap to sort the list in place
        heapq.heapify(self.minHeap)
        #Pop off excess elements to just return kth largest element
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        #Push value to the heap data structure
        heapq.heappush(self.minHeap, val)
        #Account for edge case where heap is less than k elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        #Heap is sorted, so we can return value from first index
        return self.minHeap[0]
