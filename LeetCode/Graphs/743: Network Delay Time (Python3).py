class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Djikstra's Shortest Path Algo (BFS with Min Heap)

        #Creating an Adjacent List for the nodes
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        #Initialize a minheap with first node
        minHeap = [(0, k)]

        #Set is used to check we don't visit the same node twice, Avoid Cycles!
        visit = set()

        #Create variable to store result of minimum time
        result = 0

        #Continue Algo while minHeap isn't empty
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue #We don't want to revist the same node
            visit.add(n1)
            #Update result time by accounting for weighted edge traveresed
            result = max(result, w1)

            #BFS Part, traverse neighbors and their weight
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2 + w1, n2)) #Have to add w1 to adjust for total edges
        
        return result if len(visit) == n else -1

        #TIME COMPLEXITY: O(E * logV)
