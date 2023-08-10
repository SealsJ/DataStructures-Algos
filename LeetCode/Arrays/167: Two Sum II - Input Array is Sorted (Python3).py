class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        #While loop to end search and return empty array if two pointers don't find solution
        while l < r:
            if numbers[l] + numbers[r] == target:
                #Add both values to empty result array 
                return [l + 1,r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return []
