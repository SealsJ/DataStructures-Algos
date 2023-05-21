#Creating a linear search function
def linear_search(list, target):
    """
    Returns the index position of the target if found, else return none
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

#Verify functions prints the index position if found in the list
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list.")

#Test List
numbers = [1,2,3,4,5,6,7,8,9,10]

#Testing number outside of range
result = linear_search(numbers, 12)
verify(result)

#Testing number inside of range
result = linear_search(numbers, 6)
verify(result)

#Big O notation for linear search is O(n)