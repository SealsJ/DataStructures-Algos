class Solution:
    def isValid(self, s: str) -> bool:
        #Utilize Stack Datastructure // TC: O(n) SC: O(n)
        stack = []

        #Create hashmap using closing braces as keys so we know valid pairs
        validPairs = { ')' : '(', ']' : '[', '}' : '{'}

        #Iterate through every character checking for valid pairs
        for c in s:
            if c in validPairs:
                if stack and stack[-1] == validPairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        #return True if stack is empty and all valid pairs were removed
        return True if not stack else False
