class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # if we given single strinng then asked to create 2 strings then no so the case should be len(string)<=k
        # so if k > len(s) then return. false 
        # so checking evry palindrome by partitionaing is a big task and not advised one and inefficient code so 
        # if we observe carefully theres a even number of charcters for the palindrome , except for the single char which is the middle one , elble only one b , but if we have 3 bbb then elbbble
        # annabelle where a:1 n:2 b:1 c:2 l:2
        # for the odd theres only one time it appeared so 1<=2 so possible
        # and for the leetcode l:1 e:3 t:1 c:1 , here number of the odd strings are 4 which is >k so it is not possible to create this 

        # so code
        if k > len(s):
            return False 
        # now store the frequencies of the chars 
        freqmap = [0] * 26
        for c in s:
            freqmap[ord(c) - ord('a')] += 1
        
        # to count the odd occurances 
        odd_count=0
        
        for i in range(26):
            if freqmap[i]%2!=0:
                odd_count+=1
        
        return odd_count<=k