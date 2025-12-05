class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        newarr=[]
        odd=1
        even=0
        for i in range(len(nums)):
            if(nums[i]>0):
                newarr.insert(even,nums[i])
                even=even+2
            else:
                newarr.insert(odd,nums[i])
                odd=odd+2
        return newarr