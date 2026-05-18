class TrieNode:
    def __init__(self):
        self.children={}
        # instead of array we use {} where each key is character and value is node, example for the word app 'a', 'p', 'p' are edge labels / keys the values are the nodes they point to so instead of arr[26] for avoiding space we took {} key val 
        self.is_end=False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # return the one with the smallest lexicographical order! between apple and apply we consider apple 
        # if there is no such thing then return the empty string 
        # return the word which contains all of the prefixes!!!!!!
        # keep track the longest string variable one and check whether each prefix present in the words list and if it does then return the longest 
        # we take a seperate ds trie and the flag initially is false this can be solved using the trie problem 
        # TRIE specially used to track the prefixes used is auto complete spell check and word retrieval !

        root=TrieNode() #so this will have a dict and a boolean flag 
        for word in words:
        #after completing the word we r coming back to the same root reference again 
        # after donw with apple we go for apps following we stand at the l from apple and after that we insert s as child of l  
            node=root
            for ch in word:
                if ch not in node.children:
                    node.children[ch]=TrieNode()
                # after done with it then point the reference to the node with the value its holding !
                node=node.children[ch]
            node.is_end=True
        
        # 2. after building the tree we need to search the tree and see whether we can build out of it 
        def can_build(word):
            node=root
            for ch in word:
                # traverse from top to bottom !
                node=node.children[ch]
                if not node.is_end:
                    return False
            # meaning it traversed through the entire links
            return True

        
        # now check the each word and reassign the answer everytime if it is longer !
        ans=""
        for word in words:
            if can_build(word):
                # check whether it is lexicographically small and if same length 
                if len(word) > len(ans) or (len(word)==len(ans) and word<ans):
                    ans=word
        return ans 