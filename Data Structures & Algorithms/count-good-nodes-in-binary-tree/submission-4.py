class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        stack = [(root, float("-inf"))]  # (node, max value seen on path so far)

        while stack:
            node, max_path = stack.pop()

            if node.val >= max_path:
                count += 1
                max_path = node.val

            if node.right:
                stack.append((node.right, max_path))

            if node.left:
                stack.append((node.left, max_path))

        return count