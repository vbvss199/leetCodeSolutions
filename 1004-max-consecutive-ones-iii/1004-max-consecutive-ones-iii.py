class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     count=0
    #     max_count=0
    #     for i in range(len(nums)):
    #         if(nums[i]==1):
    #             count=count+1
    #             if(count>max_count):
    #                 max_count=count
    #         else:
    #             count=0

    #     return max_count
    def longestOnes(self, nums: List[int], k: int) -> int:
        # at most k zeros can be flipped meaning change zeros to ones 
        # better way to flip zeros so that we get max consecutive ones 
        # can be solved using two pointer and sliding window 
        # brute force :check where we can flip zeros and check the length using maxConsecutiveones method out of all of them return the max length 
        # 1. try to replace the nums zeros with ones with all the possible combinations and send it to the findMaxConsecuitve funtion 
        # or generate all the subarrays with atmost k zeros using two for loops{with atmost k zeros may bhe }
        # maxLength=0
        # for i in range(0,len(nums)):
        #     zeros=0
        #     for j in range(i,len(nums)):
        #         if (nums[j]==0):
        #             zeros+=1
        #         if zeros<=k:
        #             lenSubArray=j-i+1
        #             maxLength=max(lenSubArray,maxLength)
        #         else:
        #             break
        # return maxLength
        # tc is O(n^2)
        # APPROACH 2
        # improved using sliding window and two pointer , left and right pointer stay at the same point initially 
        # the first sub array will be [1] as l and r point to the same one 
        # and a current length comes out to be l-r+1 which is 1 and zeros =0 and increment the r 
        # and check whether the number of zeros <=2 and the moment it is > k then we cannot consider the sub array , then it is where sliding window comes into the picture ! 
        # move l till it sees zeros when l=0 then remove from zeros until it is equal to k 
        # the length which is l-k+1
        # APPROACH 2
        # maxLength=0
        # right=0
        # left=0
        # zeros=0
        # while(right<len(nums)):
        #     if(nums[right]==0):
        #         zeros=zeros+1
        #     # check if it exceeds move left such that it should moved in such a way 
        #     while(zeros>k):
        #         if(nums[left]==0):
        #             zeros=zeros-1
        #         left=left+1
        #     if zeros<=k:
        #         # calculate the length 
        #         maxLength=max(maxLength,right-left+1)
        #     right=right+1
        # return maxLength 

        # the optimal solution will involve removing the sliding window 
        # same approach but need to remove the internal while loop for better TC 
        # once we reach zeros to 3 then we move the left not loosing the maxLength , if zeros are >2 then dont update the length 
        # update the length only if the zeros <=2 else increment left and check everytime if it is equal to zero !!!!
        maxLength=0
        right=0
        left=0
        zeros=0
        while (right<len(nums)):
            if(nums[right]==0):
                zeros=zeros+1
            if(zeros>k):
                if(nums[left]==0):
                    # remove the zero from zeros
                    zeros=zeros-1
                left=left+1
                # check the zeros length if it is < k then update the maxLength else no 
            if(zeros<=k):
                maxLength=max(maxLength,right-left+1)
            right=right+1
        return maxLength
