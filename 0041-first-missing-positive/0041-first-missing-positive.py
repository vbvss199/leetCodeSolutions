class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n) time meaning a single for loop and no extra space to store it 
        # array is unsorted and return the smallest positive number 
        # what if we sort the array then TC is O(log n)
        # 1 is the smallest positive integer then 2 is the one and so on ... three 
        # 2nd is 2 and 3rd is 3 and so on 
        # in this [1,2,0] 1,2 are already there so 3 is next missing  
        # to scan the missing number we need to sort the array 
        # if the array is [1,2,3] then in the worst case the smallest possible integer is 4 as 1 2 3 are present so in the worst case it is n+1
        # so doesnt matter what are the elements there but the missing positive integer ranges from [1, n+1]
        # the approach i thoight converting the array to a hashset so []->()
        # we go for every value in the rnage and check it in the hashset and return the one which is not present 
        # but the time complexity is O(n)*O(1) where O(1) is for the hashset and space will be O(n)
        
        # code!!!!!!!!!!!!!!!!!!!!!!!!
        # dont assign the nums.sort() again to itself as it returns none as it is inplace sorting 
        # nums.sort()
        # hashSet=set(nums)
        # # as the missing numbers range is from 1 to n+1
        # for i in range(1,len(nums)+1):
        #     if i in hashSet:
        #         continue
        #     else:
        #         return i
        # this needs to be done in O(1) space so better we dont use the hashet and use the same array instead !
        # points to consider using the same array so lets get rid og the negative numbers first so replace them with the 0 as other than zeoes if we keep anything then we changed the array , so if we replace then the time complexity is O(n) and for another O(n) and thirs so on which is O(3n) is still linear 
        # we use negatives to determine the element is present or not and if it is replace it with zero 

        # 1 negative numbers are useless so remove them or convert them to zeros thus is the first step 
        # give it a neutral value as it dont effect the array  and here the TIme complexity os O(n)
        # remove the numbers that cannot be possible answers 
        for i in range(0,len(nums)):
            if nums[i]<=0:
                nums[i]=len(nums)+1
        
        # 2nd step 
        # Mark presence
        for i in range(len(nums)):
            val = abs(nums[i])

            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1

        # 3rd step scan it from the 1 to n 
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1