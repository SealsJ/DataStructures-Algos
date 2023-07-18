class Solution(object):
    def maximumWealth(self, accounts):
        #Initiate a counter to keep record of the highest number
        highestSum = 0

        #Iterate through matrix, sum the value for each customer and then compare to highestSum
        for i in range(len(accounts)):
            currentSum = sum(accounts[i])
            if currentSum > highestSum:
                highestSum = currentSum
        
        return highestSum
