class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Initialized an empty dictionary to keep track of the count of elements
        hashmap = {}

        #Iterates through nums, and adds to hashmap
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        max_count = 0
        most_recurring = None

        #Iterates through hashmap, returns largest element
        for i, count in hashmap.items():
            if count > max_count:
                max_count = count
                most_recurring = i
        
        return most_recurring
