class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a default dictionary with an empty list as default
        ana = defaultdict(list)

        #For every word in the strs list, match it to the appropriate sorted version key in the dictionary
        for word in strs:
            sort = ''.join(sorted(word))
            ana[sort].append(word)

        #Return all the values of the anagram as a list to match expected output
        return list(ana.values())
