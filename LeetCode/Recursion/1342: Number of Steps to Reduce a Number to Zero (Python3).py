class Solution:
    def numberOfSteps(self, num: int) -> int:
        #Initializing base case to stop recursive calls
        if num == 0:
            return 0

        #logic to obey for 'steps' in the problem
        if num % 2 == 0:
            num /= 2
        elif num % 2 != 0:
            num -= 1

        #Recursively call adding 1 for the number of steps
        return 1 + self.numberOfSteps(num)
