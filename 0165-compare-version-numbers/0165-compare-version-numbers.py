class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # value of version is its integer conversion ignoring the leading zeros ???, comparision is from left to right 
        # revision numbers are separated by the dots the numbers after the periods are revisions and they may contain the leading not trailing zeros using lstrip() no need for lstrip as it already removes the leading zeros 
        # so 2.05 and 2.005 are same right !!!!!!!!!!
        # if version 1 > version 2then return 1 else return -1
        str1=version1.split(".")
        str2=version2.split(".")
        i,j=0,0
        while i < len(str1) or j < len(str2):
            v1 = int(str1[i]) if i < len(str1) else 0
            v2 = int(str2[j]) if j < len(str2) else 0
            if v1 < v2:
                return -1
            elif v1>v2:
                return 1
            i=i+1
            j=j+1
        return 0