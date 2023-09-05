class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Need a list to return combinations
        combos = []

        #Hashmap to store all numbers and their assigned letters
        hashmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }   

        #Declare backtracking recursive function
        def backtrack(i, curStr):
            #Create basecase to build current string
            if len(curStr) == len(digits):
                combos.append(curStr)
                return

            #map current number in digits to character
            for c in hashmap[digits[i]]:
                backtrack(i + 1, curStr + c)

        #Call recursive function if digits isn't empty
        if digits:
            backtrack(0, "")

        return combos
