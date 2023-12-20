class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        stringLength = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > stringLength:
                    stringLength = r - 1 + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
            
            #even edge case
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > stringLength:
                        stringLength = r - 1 + 1
                        res = s[l:r + 1]
                    l -= 1
                    r += 1
        
        return res

        #Starting from the center reduces Time Complexity from O(N^3) to O(N^2) comparisons
