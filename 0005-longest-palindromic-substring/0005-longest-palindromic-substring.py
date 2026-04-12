class Solution:
    def isPalindrome(self,left,right,s) -> bool:
        # check palindrome and return true 
        while(left<right):
            if(s[left]!=s[right]):
                return False
            left+=1
            right-=1
        return True
    def longestPalindrome(self, s: str) -> str:
        maxLen=0
        result=""
        for i in range(0,len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                # check whether the substring is a palindrome and if it is a palindrome then update the length 
                if (j - i + 1) <= maxLen:
                    continue
                if(self.isPalindrome(i,j,s)):
                    maxLen=j-i+1
                    result=s[i:j+1]
                    break
        return result