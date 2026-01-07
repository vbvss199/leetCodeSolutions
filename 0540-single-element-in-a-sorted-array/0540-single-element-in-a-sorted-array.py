class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(len(nums)==1):
                return nums[0]
            else:
                if(i==0):
                # the first element logic
                    if(nums[i]!=nums[i+1]):
                        return nums[i]
                elif(i==len(nums)-1):
                    # last element logic
                    if(nums[i]!=nums[i-1]):
                        return nums[i]
                else:
                    # middle elements logic 
                    if((nums[i]!=nums[i-1]) and (nums[i]!=nums[i+1])):
                        return nums[i]