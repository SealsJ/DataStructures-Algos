class Solution(object):
    def trap(self, height):
        #take care of the edge case that input is empty
        if not height:
            return 0

        #Creating two pointers and variables to store their values
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        water = 0

        #Calculate amount of water stored between two pointers
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r]) 
                water += rightMax - height[r]
        
        return water
