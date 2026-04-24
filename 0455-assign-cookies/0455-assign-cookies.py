class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m=len(g)
        n=len(s)
        l,r=0,0
        g.sort()
        s.sort()
        while(l<m and r<n):
            if(g[l]<=s[r]):
                r=r+1
                l=l+1
            else:
                r=r+1
        return l
            