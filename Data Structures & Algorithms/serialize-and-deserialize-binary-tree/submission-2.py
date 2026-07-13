# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = ''
        def dfs(node):
            nonlocal string
            if not node:
                string += 'N, '
                return
            string += str(node.val) + ', '
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if string.endswith(', '):
            string = string[:-2]
        return string
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ['1', '2', 'N', 'N', '3', '4', 'N', 'N', '5', 'N', 'N']

        data = data.split(', ')
        idx = 0
        def dfs():
            nonlocal idx
            nonlocal data
            if data[idx]=='N':
                idx+=1
                return None
            node = TreeNode(data[idx])
            idx+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        
