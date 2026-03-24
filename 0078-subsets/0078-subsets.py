# subset and subsequence the order matters in subsequence there is order 
# where in subset there is no order like [1,2] and [2,1] are treated as same 
# as [1,2] and [2,1] are same they r considered as duplicates so only [1,2] should be returned 
# usin g the power set it uses the 2*n times N for generating all the subsets using brute force 
# the optimal solution will be using the recursion 
# this solution like asking each and eveyr element to slect or not 
# as here there is no target given and we need to generate the subsets so calcualte the sum and draw base condition when sum reaches zeros then return ,but this will append all the elements 
# and the condition using pointer intiallly it points to each and every element of an array the moment sum > the array sum and it crosses the n append the ds or sum as required 
class Solution:
    def subsetsGenerator(self,nums:List[int],index,ds,results)->List[List[int]]:
        if(index==len(nums)):
            results.append(ds.copy())
            return
        # now continue with the pick and not pick logic 
        ds.append(nums[index])
        self.subsetsGenerator(nums,index+1,ds,results)
        ds.pop()
        self.subsetsGenerator(nums,index+1,ds,results)
        return results 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dont pass the sum as finding sum creates an additional O(n) TC
        return self.subsetsGenerator(nums,0,[],[])
        