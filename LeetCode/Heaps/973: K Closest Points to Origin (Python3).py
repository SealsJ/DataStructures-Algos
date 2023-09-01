class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create an empty list to store distance calculations along with points
        minHeap = []

        # For every point, calculate the distance to the origin and add it along with the point to the minHeap
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(minHeap, (distance, point))

        result = []

        # Pop the k closest points from the minHeap
        for i in range(k):
            result.append(heapq.heappop(minHeap)[1])

        return result
