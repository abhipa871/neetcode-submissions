class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val:
                if self.sameTree(node, subRoot):
                    return True

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [(root, subRoot)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True