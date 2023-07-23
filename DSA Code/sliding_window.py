def max_sum_subarray(arr, k):
    n = len(arr)

    # Check for invalid input
    if k <= 0 or k > n:
        raise ValueError("Invalid window size!")

    # Initialize variables to keep track of the window and max sum
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Start sliding the window
    for i in range(k, n):
        # Remove the element from the left end of the window
        window_sum -= arr[i - k]
        # Add the element at the right end of the window
        window_sum += arr[i]

        # Update the max_sum if necessary
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage:
arr = [2, 1, 5, 1, 3, 2]
k = 3
# result = max_sum_subarray(arr, k)
# print("Maximum sum subarray of size", k, ":", result)

def max_sum_dynamic_window(arr, max_window_size):
    n = len(arr)

    # Check for invalid input
    if max_window_size <= 0:
        raise ValueError("Invalid maximum window size!")

    # Initialize variables to keep track of the window and max sum
    window_start = 0
    max_sum = arr[0]  # Initialize max_sum with the first element of the array
    current_sum = 0

    for window_end in range(n):
        # Expand the window by adding the element at the right end
        current_sum += arr[window_end]

        # Shrink the window if the size exceeds the maximum allowed
        while window_end - window_start >= max_window_size:
            current_sum -= arr[window_start]
            window_start += 1

        # Update the max_sum if necessary
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
arr = [2, 1, 5, 1, 3, 2]
max_window_size = 3
result = max_sum_dynamic_window(arr, max_window_size)
print("Maximum sum subarray with maximum window size", max_window_size, ":", result)
