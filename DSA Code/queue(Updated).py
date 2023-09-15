"""
Queue: Implements a First-in, First-out (FIFO) order, used for BFS ALGO
We can use a deque() in Python

Time Complexity:
Enqueue (Inserting) -> O(1) .append()
Dequeue (Remove) -> O(1) .popleft()
Peek (Look at front element) O(1) list[0]
Search -> O(n) where n is the # of elements in the queue

Space Complexity:
O(n) where n is the # of elements in the queue. This accounts for the memory used to store the elements

"""
def create_queue():
    return []

def is_empty(queue):
    return len(queue) == 0

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if not is_empty(queue):
        return queue.pop(0)
    else:
        raise Exception("Queue is empty")

def peek(queue):
    if not is_empty(queue):
        return queue[0]
    else:
        raise Exception("Queue is empty")

def size(queue):
    return len(queue)

# Example usage:
queue = create_queue()
enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)

print("Queue size:", size(queue))
print("Front element:", peek(queue))

dequeued_item = dequeue(queue)
print("Dequeued item:", dequeued_item)
print("Queue size after dequeue:", size(queue))
