class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Emptry variable to store longest common prefix
        res = ""

        #Iterate up to length of first word in string
        for i in range(len(strs[0])):
            #Iterate and compare every character between words of string
            for s in strs:
              #If length of the word is equal to i, exit out to not go out of range / if letter of words don't equal then also return res
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res
