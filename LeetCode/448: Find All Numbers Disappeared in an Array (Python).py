class Solution(object):
    def findDisappearedNumbers(self, nums):
        #Create a hashset that will store all the numbers in the num array
        hashset = set()
        #Create an empty list which will hold all the numbers that are missing in nums
        missing = []

        #Adding the numbers from nums to the hashset
        for num in nums:
            hashset.add(num)

        #Iterating through the range of nums and adding to missing list if number isn't in hashset
        for num in range(1, len(nums) + 1):
            if num not in hashset:
                missing.append(num)
        
        return missing
