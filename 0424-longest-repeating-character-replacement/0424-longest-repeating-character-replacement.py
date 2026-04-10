class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen=0
        maxFreq=0
        freqMap=[0]*26
        left=0
        for right in range(len(s)):
            freqMap[ord(s[right])-ord('A')]+=1
            maxFreq=max(maxFreq,freqMap[ord(s[right])-ord('A')])
            while((right-left+1)-maxFreq>k):
                freqMap[ord(s[left])-ord('A')]-=1
                left=left+1
            maxLen=max(maxLen,right-left+1)
        return maxLen