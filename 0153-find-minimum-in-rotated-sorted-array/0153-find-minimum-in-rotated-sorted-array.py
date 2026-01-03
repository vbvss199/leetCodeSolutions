class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer=float("inf")
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            # check for the left sort
            if(nums[low]<=nums[mid]):
                # if left half is sorted update the answer with the smallest element and eliminate it
                if nums[low]<answer:
                    answer=nums[low]
                low=mid+1
            # check for the right sort
            else:
                answer=min(answer,nums[mid])
                high=mid-1
        return answer