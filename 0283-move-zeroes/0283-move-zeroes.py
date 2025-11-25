class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        count=0
        temp=[]
        for i in range(0,n):
            if(nums[i]!=0):
                temp.append(nums[i])
                count=count=1
        for j in range(0,len(temp)):
            nums[j]=temp[j]
        for k in range(len(temp),n):
            nums[k]=0

