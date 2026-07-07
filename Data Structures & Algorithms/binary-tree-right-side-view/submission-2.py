# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        s = []
        q = []
        if not root:
            return []
        while queue:
            s=[]
            qlen = len(queue)
            for i in range(qlen):
                root = queue.popleft()
                s.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            q.append(s[-1])
        return q