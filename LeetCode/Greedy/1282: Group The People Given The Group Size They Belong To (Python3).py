class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
      #Create an empty hashmap and result list to store values as we iterate through groupSizes
        hashmap = {}
        result = []

        #Enumerate to keep track of the index as well as its corresponding value when appending to hashmap
        for i, val in enumerate(groupSizes):
            if val in hashmap:
                hashmap[val].append(i)
            else:
                hashmap[val] = [i]

          #Conditional, if the length exceeds the val, we need to reset the dictionary but append already seen indexes to result
            if len(hashmap[val]) == val:
                temp_group = hashmap[val]
                hashmap[val] = []
                result.append(temp_group)
            
        return result
