class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNoteCount = {}
        magazineCount = {}

        for char in magazine:
            if char.isalpha():  # Check if the character is an alphabet letter
                char_lower = char.lower()  # Convert the letter to lowercase to handle case-insensitivity
                magazineCount[char_lower] = magazineCount.get(char_lower, 0) + 1
        
        # Step 3
        for char in ransomNote:
            if char.isalpha():  # Check if the character is an alphabet letter
                char_lower = char.lower()  # Convert the letter to lowercase to handle case-insensitivity
                ransomNoteCount[char_lower] = ransomNoteCount.get(char_lower, 0) + 1
            
        # Step 4
        for char, count in ransomNoteCount.items():
            if char not in magazineCount or count > magazineCount[char]:
                return False
            
        # Step 5
        return True
