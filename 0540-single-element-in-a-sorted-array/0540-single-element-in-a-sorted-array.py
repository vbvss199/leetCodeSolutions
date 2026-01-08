class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if(len(nums)==1):
        #         return nums[0]
        #     else:
        #         if(i==0):
        #         # the first element logic
        #             if(nums[i]!=nums[i+1]):
        #                 return nums[i]
        #         elif(i==len(nums)-1):
        #             # last element logic
        #             if(nums[i]!=nums[i-1]):
        #                 return nums[i]
        #         else:
        #             # middle elements logic 
        #             if((nums[i]!=nums[i-1]) and (nums[i]!=nums[i+1])):
        #                 return nums[i]
        # idk how and why the code got accepted even after the Time Complexity is O(n)

        # lets optimise this 
        if(len(nums)==1):
            return nums[0]
        # check for the first and last index and perform binary search trimming first and last elements
        elif(nums[0]!=nums[1]):
            return nums[0]
        elif(nums[len(nums)-1]!=nums[len(nums)-2]):
            return nums[len(nums)-1]
        # write the binary search code here !! even,odd and odd,even pairs 
        low=1
        high=len(nums)-2
        while(low<=high):
            mid=(low+high)//2
            if((nums[mid]!=nums[mid-1]) and (nums[mid]!=nums[mid+1])):
                return nums[mid]
            if(((mid%2==1) and nums[mid-1]==nums[mid]) or (mid%2==0) and nums[mid]==nums[mid+1]):
                low=mid+1
            else:
                high=mid-1