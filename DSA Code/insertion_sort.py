'''
Insertion Sort (Partial Sorting)
- For every index, put that index at the correct index of the LHS
- Time Complexity -> Worst Case: O(n^2) n = # of elements, Best Case: O(n)

Why Use it?
- Adaptive: Steps get reduces if array is sorted, number of swaps reduced compared to Bubble 
- Stable
- Used in part of hybrid sorting algorithms

'''

def insertion(nums):
    for i in range(1,len(nums)):
        j = i
        while nums[j-1] > nums[j] and j > 0:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1

    return nums

nums = [2, 6, 5, 1, 3, 4]
print(insertion(nums))