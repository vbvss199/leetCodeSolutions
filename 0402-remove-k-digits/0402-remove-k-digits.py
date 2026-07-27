class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # after removing the k digits we need to return the smallest integer of that ?
        # given string ! remove the digits in the order and return the substring which is contiguous 
        # try to remove the larger digits first which is startegy of greedy approach ,keep the smaller digits and remove the larger ones 
        # remove the larger digits by keeping track of them for which we use stack DS
        # keep the 1 in the stack then keep 4 but but for the next number 3 the 4 appears larger so replace 4 with 3 
        # as we removed the one element so k gets reduced by 1 so stack contains 1,3 now we go to the next element 
        # which is 2 and 2 is better choice than 3 we pop 3 and replace it with 2 so stack looks like 1,2
        # next element is 2 again replace that 2 with the new 2 and stack is 1,3
        # next it goes to 1 and it is even lesser than the current element so append in the stack then 
        # we go to the 9 as it is the last element keep it based on the value of the k 
        # reverse the list after the stack
        # edge cases when k is equal to the n then return the "0"
        # remove or trim the startig zeros 
        # and if the number is in increasing order remove the last k Digits from the str 
        # initalise the stack
        stack=[]

        for digit in num:
            while(stack and k >0 and stack[-1]>digit):
                stack.pop()
                # make sure we decfement the k 
                k=k-1
            stack.append(digit)

        # edge cases
        # and if the number is in increasing order remove the last k Digits from the str 
        # so nums like 123456 will end up like adding each number to the stack so remove that many elements from back  
        while(k>0):
            stack.pop()
            k=k-1
        
        # remove leading zeros      and also if we end up removing all the digits then return "0"
        # remove the leading zeros 
        res = "".join(stack).lstrip("0")

        return res if res else "0"