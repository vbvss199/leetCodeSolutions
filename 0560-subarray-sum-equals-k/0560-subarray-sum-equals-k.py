
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presummap = {0: 1}
        prefixsum = 0
        count = 0
        for i in range(0, len(nums)):
            prefixsum = prefixsum + nums[i]
            # check if there exists any other exists like in the map then again add the sum with the difference of the indices
            # now check the second condition for the remaining sum -k
            if prefixsum - k in presummap:
                count += presummap[prefixsum - k]
            if prefixsum in presummap:
                presummap[prefixsum] += 1
            else:
                presummap[prefixsum] = 1
        return count
