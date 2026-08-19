class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for bitIndex in range(0,32):
            count=0
            for i in range(len(nums)):
                if (nums[i] & (1<<bitIndex)):
                    count+=1
            if(count%3==1):
                #set the answwer bit 
                ans=ans | (1<<bitIndex)
        if ans >= (1 << 31):

            ans -= (1 << 32)

        return ans