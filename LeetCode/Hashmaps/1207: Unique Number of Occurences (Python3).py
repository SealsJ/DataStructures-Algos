class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #Initialize a counter dictionary
        hashmap = {}

        #Iterate through arr, adding key: value pairs
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        #Create a set for keys
        keySet = set(hashmap.keys())
        #Create a set for values
        valueSet = set(hashmap.values())

        #If length of keys and values are equal, no duplicates since set holds unique values (True)
        return len(keySet) == len(valueSet)
