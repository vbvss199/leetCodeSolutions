class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        strMap={}
        used=set()
        for i in range(len(s)):
            if s[i] in strMap:
                if(strMap[s[i]]!=t[i]):
                    return False
            else:
                if t[i] in used:
                    return False
                strMap[s[i]]=t[i]
                used.add(t[i])
        return True
                