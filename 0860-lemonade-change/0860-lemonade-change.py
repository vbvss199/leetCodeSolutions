class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # a variable which keep tracks of 5 10 and 15 20 add the count of 5 and 10 and so on ...
        # and to handle the cases when we encounter like for 20 the return will be 15 which is 10+5 or 5+5+5 so just make sure how we solve it 
        five=0
        ten=0
        for i in range(len(bills)):
            if(bills[i]==5):
                five=five+1
            elif(bills[i]==10):
                if(five):
                    five=five-1
                    ten=ten+1
                else:
                    return False
            else:
                if(ten and five):
                    ten=ten-1
                    five=five-1
                elif(five>=3):
                    five=five-3
                else:
                    return False
        return True