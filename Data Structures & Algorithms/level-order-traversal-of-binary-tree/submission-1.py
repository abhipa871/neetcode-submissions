# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = deque([root])
        s = []
        res = []
        while l:
            qlen = len(l)
            for i in range(qlen):
                root = l.popleft()
                if root:
                    s.append(root.val)
                    if root.left:
                        l.append(root.left)
                    if root.right:
                        l.append(root.right)
                else:
                    return []
            res.append(s)  
            s=[]
        return res
        