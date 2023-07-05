class Solution(object):
    def evalRPN(self, tokens):
        #O(n) bc we are adding and removing from singular array
        
        #Initiate the stack
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                #Order of operation matters in the case of subtration/division
                popOne, popTwo = stack.pop(), stack.pop()
                stack.append(popTwo - popOne)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                #Int function converts to integer and truncates towards zero at the same time
                popOne, popTwo = stack.pop(), stack.pop()
                stack.append(int(float(popTwo) / float(popOne)))
            else:
                #Character must be converted to integer for stack
                stack.append(int(c))
        
        return stack[0]
