class Solution:
    def generatePartitions(self,idx:int,s:str,path,results)-> List[List[str]]:
        def isPalindrome(s,l,r):
            while(l<r):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        if(idx==len(s)):
            results.append(path.copy())
            return
        for i in range(idx,len(s)):
            if isPalindrome(s,idx,i):
                path.append(s[idx:i+1])
                self.generatePartitions(i+1,s,path,results)
                path.pop()
        return results
    def partition(self, s: str) -> List[List[str]]:
        # partition the given string in such a way that each string should be a palindrome in the lists
        # partitioning again and again so we go with the recursion 
        return self.generatePartitions(0,s,[],[])