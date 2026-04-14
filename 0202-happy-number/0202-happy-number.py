class Solution:
    def get_next(self,n:int)-> int:
        return sum(int(d)**2 for d in str(n))
    def isHappy(self, n: int) -> bool:
        # replace the sum by the squares of the digit until its equal to one ! 
        # if number equals 1 then break and return true , the process ending with one is a happy number 
        slow=n
        fast=self.get_next(n)
        # loop until the fast is not equal to 1 
        while(fast!=1 and slow!=fast):
            slow=self.get_next(slow)
            fast=self.get_next(self.get_next(fast))
        return fast==1