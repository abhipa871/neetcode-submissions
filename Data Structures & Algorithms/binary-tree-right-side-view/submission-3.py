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
            rightSide = None
            qlen = len(queue)
            for i in range(qlen):
                root = queue.popleft()
                rightSide = root
                s.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            q.append(rightSide.val)
        return q