class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # to return a string instead of integer !!!!
        # we need to choose a number such that it is larger but in single digit !!!!!!!
        # need to figure out the largest integer we can construct out of the number 3, 30 we can do 330 and 303 but 330 > 303 so we consider 3 first , so when we compare treat every two integers as a sub problem 
        # but the  thing is how can we do this we convert to string and we stull compare them which will be the same 
        # 1 first and foremsot convert them to str 
        nums=list(map(str,nums))
        
        # convert them to strings first we can compare easily 
        def compare(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0
        
        nums=sorted(nums,key=cmp_to_key(compare))
        if nums[0] == "0":
            return "0"
        return "".join(nums)
        