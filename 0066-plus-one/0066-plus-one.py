class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=""
        for i in range(len(digits)):
            number=number+str(digits[i])
        # convert back the number to int then add one and split it to the array and return it 
        number=int(number)+1
        return [int(d) for d in str(number)]