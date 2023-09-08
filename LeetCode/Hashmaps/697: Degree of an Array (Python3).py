class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        #Creates a dictionary to store index and value of each number in nums
        #Left Index, Right Index, and Counter
        left, right, count = {}, {}, {}

        for i, x in enumerate(nums):
            #Stores x in left index if it doesn't exist yet
            if x not in left: left[x] = i
            #always updates right index 
            right[x] = i
            #Counter to keep track of how many times a value appeared
            count[x] = count.get(x, 0) + 1

        #Worst case, the degree would be the length of nums
        ans = len(nums)
        #Find the degree, the value that occurs most in the list
        degree = max(count.values())
        #loop through, updating answer with smaller lenghts if value of nums == degree
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
