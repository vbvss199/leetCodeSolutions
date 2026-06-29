class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # SUBSET MEANING SKIP ELEMENTS 
        # Subset or subsequence → can contain any combination of elements. You can skip elements, and they do not have to be contiguous.
        # Subarray → continuous (contiguous) elements. You cannot skip elements.
        # divide into two sub sets of equal sum 
        # if the entire sum is S and then s1 and s-S1 are two subsets with equal sum 
        # note 1 if we have a odd sum then we cannot divide into two right 
        # if even then can we divide to two with S/2 
        # GENERATING subsets -> include exlcude and back track via recursion !
        # Subset Sum equals S/2 which is same as the subset sum equals target 

        # solution walk through if it is odd then immediately return FALSE 
        
        def subSetEqualsTarget(i,target,memo):
            if(target==0):
                return True
            
            # another base case
            if(i==len(nums)):
                return target==0
            
            if (i, target) in memo:
                return memo[(i, target)]

            if nums[i] <= target:
                take = subSetEqualsTarget(i + 1, target - nums[i], memo)
            else:
                take = False

            not_take = subSetEqualsTarget(i + 1, target, memo)

            memo[(i, target)] = take or not_take

            return memo[(i,target)]

        # calculate the sum and then pass the half sum and before passing then check whether it is an odd one or even one !
        total_sum=0
        for i in range(len(nums)):
            total_sum+=nums[i]
        if(total_sum%2!=0):
            return False
        target=total_sum//2

        # so if there exists a subset whose sum is equal to the target then. return True immediately 

        # dp use memo={} which stores the target at the ith value which is. (i,target) is true or false 
        memo={}
        return subSetEqualsTarget(0,target,memo)
        

