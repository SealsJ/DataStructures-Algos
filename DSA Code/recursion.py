'''
Recursion: A function that calls itself!
Base Condition: A condition where recursion will stop making calls.
Every function call will take some memory, if no base condition, stack memory of computer runs out (Stack Overflow)

Why Recursion?
1) Helps us when solving complex problems in a simple way
2) Recursive solutions can be converted into Iterations, vice versa
3) Recursion function calls take up space, space complexity isn't constant b/c of recursive calls
'''

# def recursion(num):
#     if num == 5:
#         print(5)
#         return

#     print(num)
#     recursion(num + 1)

# recursion(1)

'''
Fibonacci Numbers:
fibo(n) = fibo(n-1) + fibo(n-2)

How to tell if we can use recursion?
1) Can we break it down into smaller parts?
2) The base condition is represented by numbers we already have
3) Understand Recurrence Relation / Recursive Tree
4) About the tree:
    See the flow of functions, how they are getting in stack, identify and focus on left and right tree calls
'''

# def fibo(n):
#     #Base Condition Neded
#     if n < 2:
#         return n

#     return fibo(n - 1) + fibo(n - 2)

# print(fibo(4))

'''
Binary Search:
F(N) = O(1) + F(N/2)

Variables: 
1) Arguments: Will go into the next function call
2) Return Type
3) Body of function: Variables that are specific to that call
'''

def binary_search(nums, target, start, end):
    if start > end:
        return -1

    middle = end - start // 2

    if nums[middle] == target:
        return middle
    elif nums[middle] < target:
        return binary_search(nums, target, middle + 1, end)
    else:
        return binary_search(nums, target, start, middle - 1)

nums = [1,2,3,4,55,66,78]

print(binary_search(nums, 90, 0, len(nums) - 1))