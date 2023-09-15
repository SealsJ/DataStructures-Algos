"""
Merge Sort: Recursive sorting algo that divides array into smaller subarrays, sorting them, then merging sorted subarrays back together to from sorted array

When to use it?
If you need a stable sorting algo that maintains O(n logn) TC and have enough memory available for the additional space needed to create temporary subarrays. (Not in-place algo)

Time Complexity:
Best Case -> O(n logn)
Worst Case -> O(n logn)

Space Complexity:
O(n) -> Need additional space up to n temporary subarrays during the merging process

"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Append any remaining elements from both halves
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
