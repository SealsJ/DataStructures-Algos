class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        resLen = 0

        for i in range(len(s)):
            #Check for even numbers
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = (s[l:r+1])
                    resLen = r - l + 1
                l -= 1
                r += 1

            #Check for odd numbers
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLEn = r - l + 1
                l -= 1
                r += 1
        
        return res
