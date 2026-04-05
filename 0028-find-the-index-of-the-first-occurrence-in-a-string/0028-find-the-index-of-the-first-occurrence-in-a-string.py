class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # based on the needle we need to split the haystack string !
        n=len(haystack)
        m=len(needle)
        for i in range(n-m+1):
            # check for the each index till the next m index
            if haystack[i:i+m]==needle:
                return i
        return -1