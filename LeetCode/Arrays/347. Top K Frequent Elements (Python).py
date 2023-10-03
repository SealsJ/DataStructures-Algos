class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create a hashmap to count number of occurences for a specific number
        hashmap = {}
        #Create buckets, for potential frequency a number can occur up to length of nums
        freq = [[] for i in range(len(nums) + 1)]
        
        #Count frequency of number in nums and store count in hashmap
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        #Take the numbers and append them to where they occured in terms of frequency
        for n, c in hashmap.items():
            freq[c].append(n)

        #Create result variable
        res = []
        #Iterate through freq in descending order return k elements
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        #TC: O(N) & SC: O(N) /// Bucket Sort Algo 
