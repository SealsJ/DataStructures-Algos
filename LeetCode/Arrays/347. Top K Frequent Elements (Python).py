class Solution(object):
    def topKFrequent(self, nums, k):
        #Bucket Sort Algo

        #Initiate Hashmap to count frequency
        count = {}
        freq =[[] for i in range(len(nums) + 1)]

        #Count how many time each # occurs in nums
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)

        #return k elements in descending order
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
