class Solution:
    def climbStairs(self, n: int) -> int:
        #Initialize two variables to keep track of subproblems
        one, two = 1, 1

        #Iterate through list of numbers to not go out of bounds
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

        #TC/SC: O(n)
