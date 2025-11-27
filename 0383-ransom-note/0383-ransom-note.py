class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table = [0] * 26
        
        # Count letters needed in ransomNote
        for char in ransomNote:
            hash_table[ord(char) - ord('a')] += 1
        
        # Subtract letters available in magazine
        for char in magazine:
            hash_table[ord(char) - ord('a')] -= 1
        
        # Check if any letter is needed but not available (negative count)
        for count in hash_table:
            if count > 0:        # > 0 means "still needed, but not in magazine"
                return False     # Wait! This is the key!
        
        return True              # All counts <= 0 → we have enough