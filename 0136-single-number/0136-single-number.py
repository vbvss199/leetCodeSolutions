class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mpp={}
        for num in nums:
            mpp[num]=mpp.get(num,0)+1
        for num,count in mpp.items():
            if(count==1):
                return num

        