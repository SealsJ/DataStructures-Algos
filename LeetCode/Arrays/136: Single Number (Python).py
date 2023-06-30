class Solution(object):
    def singleNumber(self, nums):
        #Establishing a dictionary for just integers
        frequency = defaultdict(int)

        #Iterating through nums to add the frequency of each # to dictionary
        for i in nums:
            frequency[i] += 1

        #If # only appeared once in dictionary, we will return it
        for i in frequency:
            if frequency[i] == 1:
                return i
