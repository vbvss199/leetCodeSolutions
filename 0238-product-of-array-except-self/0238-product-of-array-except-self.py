class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefProduct = [1] * n
        suffProduct = [1] * n
        res = [0] * n
        for i in range(1,n):
            prefProduct[i]=prefProduct[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suffProduct[j]=suffProduct[j+1]*nums[j+1]
        for k in range(n):
            res[k]=prefProduct[k]*suffProduct[k]
        return res
