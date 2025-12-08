from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxElement = float("-inf")
        temp = [-1]
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > maxElement and arr[i - 1] > arr[i]:
                maxElement = arr[i]
                temp.append(maxElement)
            else:
                maxElement = max(maxElement, arr[i])
                temp.append(maxElement)
        return temp[::-1]

