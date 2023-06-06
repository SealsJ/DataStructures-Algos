#

def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log n)time / Linear Space complexity
    """

    if len(list) <= 1:
        return list #Technically already sorted and no work is needed (This is our stopping condition)

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


#Divide Step
def split(list):
    """Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes overall O(log n) time
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


#Sorting/Merging the arrays
def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    Runs in overall O(n) time
    """

    #creating local values to keep track of index values
    l = []
    i = 0 #track index of left list
    j = 0 #track index of right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i +=1
        else:
            l.append(right[j])
            j += 1


    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


testList = [234, 12, 45, 76, 9, 14, 39]
x = merge_sort(testList)
print(x)

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


#Testcase
testList = [54, 30, 12, 1, 65, 76, 234]
x = merge_sort(testList)
print(verify_sorted(testList))
print(verify_sorted(x))
