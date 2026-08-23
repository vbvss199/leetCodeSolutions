class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # school concept like simple adding using carry and sum varibles !! lets see 
        # using carry and sum variables 
        carry=0
        res=""
        # as we start from the end so reverse the digits 
        a,b=a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            digitA=ord(a[i])-ord('0') if i <len(a) else 0
            digitB=ord(b[i])-ord('0') if i < len(b) else 0
            total=digitA+digitB+carry

            # what we will be adding to the result now ? so we wanna add either 1 or 0 so we mod them 
            char=str(total % 2)
            res=char+res
            # update the carry which is //2
            carry=total//2
        if carry:
            res="1"+res
        return res