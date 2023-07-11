class Solution(object):
    def maxProfit(self, prices):
        #Create a left and right pointer
        l, r = 0, 1
        #This will store the maximum profit we find as we iterate through array
        maxProfit = 0

        #Iterating until the right pointer reaches end of array
        while r < len(prices):
            #This indicates profit if right pointer value is greater than left, calculate it
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                #Use max function to test if new profit is the "MAX" profit of array
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1

        return maxProfit
