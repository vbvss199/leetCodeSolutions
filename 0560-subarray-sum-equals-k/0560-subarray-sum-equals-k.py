
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presummap = {}
        presummap[0]=1
        prefixsum = 0
        count = 0
        for i in range(0, len(nums)):
            # first step the intiial sum
            prefixsum = prefixsum + nums[i]
            # check if there exists any other exists like in the map then again add the sum with the difference of the indices
            # now check the second condition for the remaining sum -k
            # check for prefixsum-k
            if prefixsum - k in presummap:
                count += presummap[prefixsum - k]
            # else addd the current prefixsum to the map
            if prefixsum in presummap:
                presummap[prefixsum] += 1
            else:
                presummap[prefixsum] = 1
        return count

        # lets try the two pointer approach
        # left=0 
        # right=0
        # sum =nums[0]
        # count=0
        # while(right<len(nums)):
        #     while(left<=right and sum>k):
        #         sum=sum-nums[left]
        #         left=left+1 
        #     if(sum==k):
        #         count=count+1
        #     right=right+1
        #     if(right<len(nums)):
        #         sum=sum+nums[right]
        # return count

# the above 2nd method will work only if there are positive numbers in the arry