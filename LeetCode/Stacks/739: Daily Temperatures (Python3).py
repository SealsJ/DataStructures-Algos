class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #TC: O(N) Monotonic Decreasing Stack
        ans = [0] * len(temperatures)
        stack = [] #pair values: [temp, index value]

        #Storing index, temperature pairs into stack
        for i, t in enumerate(temperatures):
            #While the stack isn't empty and the temperature at top of stack is greater than current T
            while stack and t > stack[-1][0]:
                #Pop the values from stack and then calculate number of days to be added to result
                stackT, stackInd = stack.pop()
                ans[stackInd] = (i - stackInd)
            #append any values if stack is empty
            stack.append([t, i])
            

        return ans
