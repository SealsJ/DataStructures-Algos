class Solution(object):
    def sortedSquares(self, nums):
        #Creating an empty array to store the squared values
        squared = []

        #iterate through each value squaring the result
        for i in nums:
            squared.append(i * i)
        
        #return the sorted array
        return sorted(squared)
