# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # stack = [root]
        # s=[]
        # while stack:
        #     root = stack.pop()
        #     s.append(root.val)
        #     if root.right:
        #         stack.append(root.right)
        #     if root.left:
        #         stack.append(root.left)
        # print(s)    
        count = 0
        def dfs(node, max_path):
            nonlocal count
            if not node:
                return None
            if node.val>=max_path:
                max_path = node.val
                count+=1

            dfs(node.left, max_path)
            dfs(node.right, max_path)
        dfs(root, float('-inf'))
        return count