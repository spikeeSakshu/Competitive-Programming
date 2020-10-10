'''
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        self.data = ''
        def dfs(node):
            if node:
                self.data += '%s ' % node.val
                dfs(node.left), dfs(node.right)
            else: self.data += '# '
        dfs(root)
        return self.data
        
    def deserialize(self, data):
        def dfs():
            val = next(data)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left, node.right = dfs(), dfs()
            return node
        data = iter(data.split())
        return dfs()
    
#     def serialize(self, root: TreeNode, file= []) -> str:
#         """Encodes a tree to a single string.
#         """
#         if root: 
#              # then print the data of node 
#             file.append(str(root.val))
            
#             self.serialize(root.left, file)
#             self.serialize(root.right, file) 
        
#         return ','.join(file)
#     def deserialize(self, data: str) -> TreeNode:
#         """Decodes your encoded data to tree.
#         """
#         iterator = iter(data.split(','))
#         def buildTree():
            
#             node = next(iterator)
            
#             if node == '':
#                 return None
#             print('node', node)
#             ans = TreeNode(int(node))
#             ans.left = buildTree()
#             ans.right = buildTree()
#             return ans
#         return buildTree()  
    
#         data= data.split(',')
        
#         if data[0]=='':
#             return
        
#         root= TreeNode(data.pop(0))
#         root.left= self.deserialize(','.join(data))
#         root.right= self.deserialize(','.join(data))
        
#         return root
        
#         root = TreeNode(val); 
#         deSerialize(root->left, fp); 
#         deSerialize(root->right, fp); 
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans