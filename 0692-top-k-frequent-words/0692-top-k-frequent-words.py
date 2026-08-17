class Pairs:
    def __init__(self, string, freq):
        self.string=string
        self.freq=freq
    # custom comparator operator 
    def __lt__(self,other):
        # condition when both the strings are equal 
        if(self.freq==other.freq):
            return self.string < other.string
        # then return the one 
        return self.freq > other.freq

# using min heap 
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # using Counter make the hashmap
        freqs=Counter(words)
        # now create a array of object pairs which will comapre using the comparator operator 
        obj_pairs=[Pairs(key,val) for key,val in freqs.items()]

        # now using the heapq heapify 
        heapq.heapify(obj_pairs)

        # the heap is still stored inside the obj_apoirs

        # now they r rearranged to satisfy the heap property 
        result=[]
        for _ in range(k):
            pair=heapq.heappop(obj_pairs)
            result.append(pair.string)

        return result
