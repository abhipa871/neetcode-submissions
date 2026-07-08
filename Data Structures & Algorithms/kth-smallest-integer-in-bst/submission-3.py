class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None

        def inorder(node):
            nonlocal count, answer

            if not node or answer is not None:
                return

            inorder(node.left)

            count += 1
            if count == k:
                answer = node.val
                return

            inorder(node.right)

        inorder(root)
        return answer