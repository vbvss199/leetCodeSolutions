class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s and t consist of lowercase English letters. so they have same ASCII values 
        hash_table1=[0]*26
        hash_table2=[0]*26
        for i in s:
            hash_table1[ord(i)-ord('a')]+=1
        for j in t:
            hash_table2[ord(j)-ord('a')]+=1

        if(hash_table1==hash_table2):
            return True 
        else:
            return False 
