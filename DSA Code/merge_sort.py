'''
Merge Sort (Recursion)
- Divide Array into 2 parts, sort 1st half, then 2nd, merge them together
1) Divide Array into 2 Parts
2) Get Both Parts Sorted via recursion
3) Merge Sorted Parts (When one array empties, add the rest of first array to end)

Time Complexity -> O(nlogn) // Space -> O(n)
'''

def merge_sort(nums):
    if len(nums) == 1:
        return nums

    left = nums[:len(nums)//2]
    right = nums[len(nums)//2:]

    #Recursion
    merge_sort(left)
    merge_sort(right)

    # Merge Left and Right
    i = 0 #Left Index
    j = 0 #Right Index
    k = 0 #Keeps track of index in merged array

    #Run these until they are out of bounds
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    #If one of the arrays is a different size, copy the remaining elements
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k +=1

    return nums

nums = [5, 4, 3, 2, 1]
print(merge_sort(nums))

