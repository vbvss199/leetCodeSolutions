# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # return type is string 
        if not root:
            return ""
        bstr=[]
        queue=deque()
        queue.append(root)
        while(queue):
            node=queue.popleft()
            if node is None:
                bstr.append("#")
            else:
                bstr.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(bstr)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        # convert the str back to array where each string represnts the each node val
        dataArr=data.split(",")
        # dataArr looks like ["1","2,"3","#",.....]
        root = TreeNode(int(dataArr[0]))
        queue=deque()
        queue.append(root)
        i=1
        while(queue and i <=len(dataArr)):
            node=queue.popleft()
            if dataArr[i] =="#":
                node.left =None
            else:
                # create a tree node with the dataArr element !and attach it as left element
                leftelement=TreeNode(int(dataArr[i]))
                node.left=leftelement
                queue.append(leftelement)
            i=i+1
            #right
            if dataArr[i]=="#":
                node.right =None
            else:
                rightelement=TreeNode(int(dataArr[i]))
                node.right=rightelement
                queue.append(rightelement)
            i=i+1
        return root 
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))