class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list) #mapping the count of characters to the list of anagrams

        for s in strs:
            count = [0] * 26 #one for each character (a -> z)

            for c in s:
                count[ord(c) - ord("a")] += 1 #Taking ASCII value of "a" to map each character appropriately to the right index

            hashmap[tuple(count)].append(s) #lists cant be keys but tuples can be
            
        return hashmap.values()
