class Solution:
    def reverseWords(self, s: str) -> str:
        # /instead of strip if we use splitWhen you use split() without any argument, Python does not use a specific separator character. Instead, it splits on any whitespace and treats consecutive whitespace as a single separator.
        # split removes the trailing and ending spaces # 
        # then change the strip to array of string and print in the reverse direction
        words=s.split()
        # taking them in the reverse direction and joinining using the .join
        result=" ".join(words[::-1])
        return result