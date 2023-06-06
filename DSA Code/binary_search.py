#Creating a binary search function
def binary_search(list, target):
    #finding the first position of the list
    first = 0
    #finding the last position of the list
    last = len(list) - 1

    while first <= last:
        #find midpoint with floor division, round down to nearest whole number
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list.")

#Test List / list must be sorted based on the logic of a binary search
numbers = [1,2,3,4,5,6,7,8,9,10]

#Testing number outside of range
result =  binary_search(numbers, 12)
verify(result)

#Testing number inside of range
result = binary_search(numbers, 6)
verify(result)

#iterative version of binary search takes constant space amount of memory
#run time is O(log n), algorithm takes an additional step each time the data doubles
