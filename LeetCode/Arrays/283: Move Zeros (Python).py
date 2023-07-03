class Solution(object):
    def moveZeroes(self, nums):

        #Iterate from the end of the list, pop off 0s and append them to end of list
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)

        return nums


        #Two pointer solution without using more memory
        leftPointer = 0
        for rightPointer in range(len(nums)):
            #Perform a swap if the number is a 0
            if nums[rightPointer]:
                nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]
            l += 1
        
        return nums
