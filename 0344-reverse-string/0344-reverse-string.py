class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # i=0
        # j=len(s)-1
        # while(i<j):
        #     s[i],s[j]=s[j],s[i]
        #     i=i+1
        #     j=j-1
        # return s

        # lets do the same operation with recursion 
        #function(l,r) swap(l,r) function(l+1,r-1) and the base condition is if(l>=r): return 
        def recursiveReverseString(left,right):
            if left>=right:
                return
            s[left],s[right]=s[right],s[left]
            recursiveReverseString(left+1,right-1)
        recursiveReverseString(0,len(s)-1)