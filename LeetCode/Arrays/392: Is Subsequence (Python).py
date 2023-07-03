class Solution(object):
    def isSubsequence(self, s, t):
        #Creating the pointers for iterating through both strings (s,t)
        i, j = 0, 0

        #Iterate through strings while being less than their total length
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        #If I = len(s), we found all characters of the substring
        return True if i == len(s) else False

        #True means we found every character
        #False means we went out of bound of j and didn't
