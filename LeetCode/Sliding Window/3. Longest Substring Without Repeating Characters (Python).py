class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #Initiate a hashset to check for duplicate characters
        hashset = set()
        l = 0
        result = 0

        #Increment the right pointer through the length of string
        for r in range(len(s)):
            #if right pointer reaches character in hashset, remove it and adjust left pointer
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            #Determine the max result of current result vs previous results
            result = max(result, r - l + 1)
        return result
