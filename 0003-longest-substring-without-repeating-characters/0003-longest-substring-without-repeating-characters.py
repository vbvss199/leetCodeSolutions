class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using sliding window and two pointer 
        # any portion of the string which is consecutive   
        # if we consider any sub string it must be the max length and we need to return the length 
        # extreme naive generate all the substrings using two loops then check which are unique and have the max length then return it 
        # for (i=0 ;i<n;i++)
        # for (j=i ;j<n;j++)
        # sub=sub+s[j] 
        # and we make sure there are no repeating characters inside the each substring 
        # and we check if there is a repeating charcter theres no point to generate a sub string with the duplicate so we break that sub string and go to next iteratiion  
        # use a hasharray to track the repeated element  using hash[255]=[0]
        # hash=[0]*255
        # we check the jth character as i is constant for the sub array !
        # if hash[s[j]]==1: then break the loop 
        # hash[ord(ch)] += 1
        # compute the length which is j-i+1 then compare it with the maxLength and swap it if it is greater else same 

        # lets code !
        maxLength=0
        subStr=""
        # and a hash to keep track of the charcters counts 
        for i in range(0,len(s)):
            # for everysubstring we see if there is any repeating char in that substring
            hash=[0]*256
            for j in range(i,len(s)):
                # subStr=subStr+s[j]
                # we never use this substr
                hash[ord(s[j])]+=1
                if(hash[ord(s[j])]>1):
                    break
                substrLen=j-i+1
                maxLength=max(maxLength,substrLen)
        return maxLength
                


