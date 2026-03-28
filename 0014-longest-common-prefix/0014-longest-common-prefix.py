class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for s in strs:
                if i >=len(s) or  s[i]!=strs[0][i]:
                    return strs[0][:i]
        # this one when the loop reaches the end where we need to return the first element but un the start it wont run as it contain a empty string 
        return strs[0]