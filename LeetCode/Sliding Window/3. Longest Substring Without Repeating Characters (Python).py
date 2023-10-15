class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #Sliding Window Solution // TC: O(n), SC: O(n)

        #Create a set to store unique characters in our window
        testSet = set()

        #Utilize two pointers, one left, one right in for loop, create a result variable
        l = 0
        res = 0

        for r in range(len(s)):
            #while duplicated value is in set, remove it and adjust left pointer
            while s[r] in testSet:
                testSet.remove(s[l])
                l += 1
            testSet.add(s[r])
            #calculate max length between current max and new updated length of left/right pointers
            res = max(res, r - l + 1)

        return res
