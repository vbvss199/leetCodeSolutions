class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results=[]
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left=self.diffWaysToCompute(expression[0:i])
                right=self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i]=="+":
                            results.append(l+r)
                        elif expression[i]=="-":
                            results.append(l-r)
                        else:
                            results.append(l*r)
        # base case
        if not results:
            results.append(int(expression))
        return results