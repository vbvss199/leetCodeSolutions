class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reverse the string and it reads the same then return true  
        def isPalindromeRecursive(left,right):
            if(left>=right):
                return True
            # write the base case 
            if(s[left]!=s[right]):
                return False
            return isPalindromeRecursive(left+1,right-1)
        # make sure to split the array using split
        s=[c.lower() for c in s if c.isalnum()]
        left=0
        right=len(s)-1
        return isPalindromeRecursive(left,right)