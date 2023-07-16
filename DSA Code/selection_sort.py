'''
Selection Sort
Time Complexity -> Worst Case: O(n^2),  Best Case: O(n^2)
Use Case: Performs well on samll lists/arrays

Pick an element and move it to right index in array
1) Find the Maximum/Minimum Value of an array
2) Swap index with correct index of array

'''

def selection(nums):

    for i in range(len(nums) - 1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
            
        nums[i], nums[minpos] = nums[minpos], nums[i]

    return nums


nums = [5, 3, 8, 6, 7, 2]
print(selection(nums))