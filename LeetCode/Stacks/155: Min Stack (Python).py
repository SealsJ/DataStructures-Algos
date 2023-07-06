class MinStack(object):

    def __init__(self):
        #Initializing two stacks, both are empty
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        #Take minimum value of value and minimum stack if minimum stack isn't empty
        val = min(val, self.minStack[-1] if self.minStack else val)
        #If minstack is empty
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
        
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]
        
#Top and getMin are only called if stack contains values so don't need to consider edgecases
