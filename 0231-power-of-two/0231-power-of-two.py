class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # to check the given number is power of two, lets do first with recursion then optimise 
        if(n<=0):
            return False
        if(n==1):
            return True
        if(n%2!=0):
            return False
        else:
            return self.isPowerOfTwo(n//2)