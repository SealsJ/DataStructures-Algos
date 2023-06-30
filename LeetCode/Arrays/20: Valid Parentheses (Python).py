class Solution(object):
    def isValid(self, s):
        #Creating an empty stack
        stack = []
        #Creating a hashmap to identify correct pairs
        hashmap = { ')' : '(',
                    '}' : '{', 
                    ']' : '['}

        #Use for loop to iterate through each character in string
        for i in s:
            if i in hashmap:
                #Iterates for closing characters 
                if stack and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
            #If first character is an opening character
            else:
                stack.append(i)

        #Return true for valid strings if not empty
        return True if not stack else False
