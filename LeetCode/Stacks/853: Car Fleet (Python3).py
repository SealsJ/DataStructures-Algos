class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Time Complexity: O(n)

        #Creating an array of pairs for position and speed
        pair = [[p,s] for p,s in zip(position, speed)]


        #stack will inform us how many fleets we have at the end
        stack = []

        #Reverse sorting to start with car closest to target
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p)/ s) #time it would take to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
