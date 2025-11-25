class Solution:
    def rev(self,nums,left,right):
        while(left < right):
            nums[left],nums[right]=nums[right],nums[left]
            left=left+1
            right=right-1
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        self.rev(nums,0,n-1)
        self.rev(nums,0,k-1)
        self.rev(nums,k,n-1)