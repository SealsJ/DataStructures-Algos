'''
Bubble Sort:
Time Complexity: Worse Case -> O(n^2) Best Case -> O(n)
Space Complexity: O(1)
'''

'''
We want to perform swapping n - 1 times bc first position is 
auto sorted if the rest are sorted (Nested Loops)

Have to iterate through entire list, except last element bc
there isn't a number after it to compare it to (len(elements)#-1)
- i is to improve efficiency of algo, don't need to resort
Swaped mechanic to stop function if list is already sorted
'''
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        swapped = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break
        

nums = [88, 9 , 2]
bubble_sort(nums)
print(nums)
