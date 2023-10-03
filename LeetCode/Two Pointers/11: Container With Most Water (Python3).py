class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Two Pointer Solution O(n)
        left, right = 0, len(height)- 1
        area = float(-inf)

        #While left pointer is less than the right pointer
        while left < right:
            #Calculate the distance between the two points
            distance = right - left

            #If left pointer is less than right, area can only be as tall as smallest border
            #We multiple left height by distance between pointers and update left pointer
            if height[left] < height[right]:
                currArea = height[left] * distance
                left += 1

            #If right pointer is less than left, area can only be as tall as smallest border
            #We multiple right height by distance between pointers and update right pointer
            elif height[left] >= height[right]:
                currArea = height[right] * distance
                right -= 1

            #Keep track of max area as pointers iterate through
            area = max(area, currArea)

        return area
