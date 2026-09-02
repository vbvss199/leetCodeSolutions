class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        resultSum=nums[0]+nums[1]+nums[2]
        differencetarget=0
        minDifference=float("inf")
        for i in range(0,len(nums)-2):
            # using two pointers
            left=i+1
            right=len(nums)-1
            sum=0
            while(left<right):
                sum=nums[i]+nums[left]+nums[right]
                
                # check if the sum is equal to the target
                if(sum==target):
                    return target
                if(sum<target):
                    left=left+1
                else:
                    right=right-1
                differenceToTarget=abs(sum-target)
                if(differenceToTarget<minDifference):
                    resultSum=sum
                    minDifference=differenceToTarget
                
        return resultSum