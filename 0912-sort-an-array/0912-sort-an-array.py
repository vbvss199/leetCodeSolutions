class Solution:
    def merge(self, nums, start, mid, end):
        temp=[]
        i=start
        j=mid+1
        while((i<=mid) and (j<=end)):
            if(nums[i]<=nums[j]):
                temp.append(nums[i])
                i=i+1
            else:
                temp.append(nums[j])
                j=j+1
        while(i<=mid):
            temp.append(nums[i])
            i=i+1
        while(j<=end):
            temp.append(nums[j])
            j=j+1
        for k in range(len(temp)):
            nums[start+k]=temp[k]
        
    def mergesort(self,nums,start,end):
        if (start < end):
            mid=(start+end)//2
            self.mergesort(nums,start,mid)
            self.mergesort(nums,mid+1,end)
            self.merge(nums, start, mid, end)
    def sortArray(self, nums: List[int]) -> List[int]:
        start=0
        end=len(nums)-1
        # step1 dividing arrays into two parts and sending them to merge formuale
        self.mergesort(nums,start,end)
        return nums
    

        