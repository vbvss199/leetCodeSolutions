class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            hash_table=[0]*26
            for i in ransomNote:
                hash_table[ord(i)-ord('a')]+=1
            for j in magazine:
                hash_table[ord(j)-ord('a')]-=1

            for i in hash_table:
                if(i>0):
                    return False 
            return True 