class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        # for i in range(len(haystack) + 1 - len(needle)):
        #     for j in range(len(needle)):
        #         if haystack[i + j] != needle[j]:
        #             break
        #         if j == len(needle) - 1
        #             return i

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        
        return -1


    #Time Complexity: O(n * m)
