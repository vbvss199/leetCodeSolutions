class Solution:
    def intToRoman(self, num: int) -> str:
        # return roman str is the output !
        # lets start small so 5 is given then append in reverse so 4 or 9 given then append in reverse 
        values = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]
      
    #   so take the number and do iteration and take a empty string 
        roman_str=""
        for val,symbol in values:
            while num>=val:
                roman_str=roman_str+symbol
                num=num-val
        return roman_str
    
    # if number is 3000 then while loop may run 3 times so outer loop stilll says one