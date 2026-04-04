class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # we need to return the count where the substring containing all the chars a b c 
        # naive approach will be generate all the substrings and check if the substring contains a & b & c then increment the count !!!!!
        # count=0
        # for i in range(0,len(s)):
        #     freq = [0] * 3
        #     for j in range(i,len(s)):
        #         freq[ord(s[j])-ord('a')]=1
        #         # write a condition to check if the given subStr contains a &b&cthen. increment the count and return it 
        #         if(freq[0]+freq[1]+freq[2]==3):
        #             # after getting a valid substring then the every substring beyond it will be also a valid substring so thats why we add the remaining charcters to the answer !
        #             count=count+(len(s)-j)
        #             break
        # return count
        # this will fail due to O(n2) time complexity !

        # lets see the optimal approach using two pointer 
        # APPROACH 2:
        # we need to make sure we get a window which has all the three chars  
        count=0
        left=0
        right=0
        count=[0]*3
        # result to store the number of substr
        result=0
        for right in range(len(s)):
            count[ord(s[right])-ord('a')]+=1
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                result += len(s) - right #all substrings are valid 
                # we then make a move to the left side searching for other substrings 
                count[ord(s[left])-ord('a')]-=1
                left=left+1
        return result
              