"""
Time Complexity:
Best Case -> O(1) , target element is found at the middle of the array
Worse Case -> O(logn), target element is at the ends of the array, have to make log(n) comparisons cutting array in half

Space Complexity:
O(1) because it only requires constant space for variables regardless of input size

When to use it?
You need to find a specific element in an array which is sorted (either ascending or descending)

"""

#Iterative Approach
def binary_search(nums, target):
  #Define Left and Right Index
  left, right = 0, len(nums) - 1

  while left <= right:
    #Create middle index we use for searching
    mid = (left + right) // 2

    if nums[mid] == target:
      return mid #Target is found
    elif nums[mid] < target:
      left = mid + 1 #Target is in the right half
    else:
      right = mid - 1 #Target is in the left half
    
  return -1 #Target isn't found

#Recursive Approach
def recursiveBS(nums, left, right, target):
  if left <= right:
    mid = (left + right) // 2

    if nums[mid] == target: #Target is found
      return mid
    elif nums[mid] < target: #Target is in the right half
      return recursiveBS(nums, mid + 1, right, target)
    else: #Target is in the left half
      return recursiveBS(nums, left, mid - 1, target)
  
  return -1 #Target wasn't found

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3
print(binary_search(nums, target))
print(recursiveBS(nums, 0, len(nums) - 1, target))
