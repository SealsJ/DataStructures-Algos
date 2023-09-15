"""
Stack: Maintains a last-in, first-out (LIFO) order // Implementation for DFS ALGOS

Time Complexity:
Push(insertion) -> O(1) .append() in Python
Pop(Deletion) -> O(1) .pop() in Python
Peek(Look at top element) -> O(1) // Make function to look at list[-1]
Search -> O(n) in the worst case where n is the # of elements in the stack

Space Complexity:
O(n) where n is the # of elements in the stack. Accounts for memory to store stack
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Top element:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack size after pop:", stack.size())
