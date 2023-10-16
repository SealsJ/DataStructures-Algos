class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Create a hashmap to store the count of numbers in the string s
        count = {}
        result = 0

        #Use Sliding Window Technique, with l and r pointer, to iterate through s
        l = 0
        for r in range(len(s)):
            #Updating hashmap with frequency of occuring letter
            count[s[r]] = 1 + count.get(s[r], 0)

            #while length of window - max frequency of reoccuring letter is greater than k
            #Meaning our window is no longer valid, we need to shrink from left side
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            #Update result of max valid window
            result = max(result, (r - l + 1))

        return result

        #Solution has TC: O(26N) 26 refers to max letters from alphabet


    #Optimal TC: O(N) Solution / utilizes maxf variable to keep track instead of scanning entire hashmap
        count = {}
        result = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
          
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, (r - l + 1))

        return result

  
