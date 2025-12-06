class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=-1
        # problem is defined in three steps
        # 1 find the break point
        # the least break pooint can be found from the n-2 point 
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<nums[i+1]):
                index=i
                break
        if(index==-1):
            return nums.reverse()
            return
        else:
            for i in range(len(nums)-1,-1,-1):
                if(nums[i]>nums[index]):
                    nums[i],nums[index]=nums[index],nums[i]
                    break
            nums[index+1:]=nums[index+1:len(nums)][::-1]
            
        #  2 swap the index element with the one less than the index comparing to the right
        # 3 finally reverse the array nxt to the i i.e from i+1
        