class Solution(object):
    def isPalindrome(self, s):
        #Creating a pointer for the left and right side of the string
        left = 0
        right = len(s) - 1

        #Creating while loop to iterate through the string until the left and right pointers equal 
        while left < right:
            #Check both characters are alphanumeric
            while left < right and not self.alphaNum(s[left]):
                left +=1
            
            while right > left and not self.alphaNum(s[right]):
                right -=1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        #return True if the string is a valid palindrome
        return True    

    #Removing special characters based on ASCII Value
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))
