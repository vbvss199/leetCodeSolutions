class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # # better approach failing 2 test cases passed 189/191 
        # maxProduct=float("-inf")
        # for i in range(0,len(nums)):
        #     product=1
        #     for j in range(i,len(nums)):
        #         product=product*nums[j]
        #         maxProduct=max(product,maxProduct)
        # return maxProduct
        suffix=1
        prefix=1
        n=len(nums)
        maxProduct=float("-inf")
        for i in range(n):
            if(suffix==0):
                suffix=1
            if(prefix==0):
                prefix=1
            prefix=prefix*nums[i]
            suffix=suffix*nums[n-i-1]
            maxProduct=max(suffix,maxProduct)
            maxProduct=max(prefix,maxProduct)
        return maxProduct