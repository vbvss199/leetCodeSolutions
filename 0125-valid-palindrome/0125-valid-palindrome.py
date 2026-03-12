class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reverse the string and it reads the same then return true  
        def isPalindromeRecursive(i):
            if(i>=n/2):
                return True
            # write the base case 
            if(s[i]!=s[n-i-1]):
                return False
            return isPalindromeRecursive(i+1)
        # make sure to split the array using split
        s=[c.lower() for c in s if c.isalnum()]
        n=len(s)
        return isPalindromeRecursive(0)