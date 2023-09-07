def combos(nums):
    def generate_subsets(start_index, current_path):
        # Add the current subset to the result
        combos.append(current_path[:])
        
        # Explore all possible subsets starting from the current_index
        for i in range(start_index, len(nums)):
            current_path.append(nums[i])
            
            # Recursively generate subsets with the next element
            generate_subsets(i + 1, current_path)
            
            current_path.pop()  # Backtrack by removing the last element

    combos = []
    generate_subsets(0, [])
    return combos

# Example usage
nums = [1, 2, 3]
result = combos(nums)
print(result)
