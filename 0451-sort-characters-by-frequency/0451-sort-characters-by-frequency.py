class Solution:
    def frequencySort(self, s: str) -> str:
        mpp = {}
        for c in s:
            mpp[c] = mpp.get(c, 0) + 1
        # map.items returns the list with iterable tuples
        # {'t':1,'r':1,'e':2}=>[('t',1),('r',1),('e',2)]
        # sorted is applied for the list
        # When comparing two items, don’t compare the whole tuple —instead, compare only the result of something
        sorted_chars = sorted(mpp.items(), key=lambda x: x[1], reverse=True)
        # now the list is [('e',2),('t',1),('r',1)]
        # we need to join this list
        return "".join(c * freq for c, freq in sorted_chars)