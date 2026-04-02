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
        # maxLength=0
        # subStr=""
        # # and a hash to keep track of the charcters counts 
        # # APPROACH 1
        # for i in range(0,len(s)):
        #     # for everysubstring we see if there is any repeating char in that substring
        #     # if we r unaware of the ascii values its safe to consider all of them which is 255 
        #     # we can use hash=[0]*26 to make them to a scale of 0-25 we remove it from ord('a')
        #     # and the logic changes as hash[ord(s[j])-ord("a")], freq[ord(s[j]) - ord('a')] += 1
        #     hash=[0]*256
        #     for j in range(i,len(s)):
        #         # subStr=subStr+s[j]
        #         # we never use this substr
        #         hash[ord(s[j])]+=1
        #         if(hash[ord(s[j])]>1):
        #             break
        #         substrLen=j-i+1
        #         maxLength=max(maxLength,substrLen)
        # return maxLength
        # this approach consumes o(n^2) time complexity , we use two pointer along with the sliding window algorithm 
        # APPROACH 1 END 


        # initially l=0 r=0 the substring is between l to r 
        # maintain a hashmap for the charcter and index to check whether it is repeating or not , maxlen=0  and the substring length calculated by l-r+1
        # if the element is found then go to the place or index ahead of it supose 
        # cadbzabcd ; l and r at same place we increment r the moment r is at "a" next to z is already in the map so move left by left=mpp.get("a") +1 then again check length and move on.  
        # and update the index of a by 1  

        # APPROACH 2 
        left=0
        right=0
        maxLen=0
        # and a hashArray to store the indices 
        hash=[-1]*256
        while(right < len(s)):
            # in the map condition 
            if(hash[ord(s[right])]!=-1):
                # and if hash[right] which is index > =l then updaye the left by 1 
                if(hash[ord(s[right])]>=left):
                    # move the left pointer by 1 
                    left=hash[ord(s[right])]+1
            subStrLen=right-left+1
            maxLen=max(subStrLen,maxLen)
            hash[ord(s[right])]=right 
            right=right+1
        return maxLen