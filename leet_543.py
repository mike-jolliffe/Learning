# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = 1

    def diameterOfBinaryTree(self, root):
        """Return max number of edges to get from any node to another
        :type root: TreeNode
        :rtype: int
        """

        self.depth(root)
        return self.ans - 1

    def depth(self, node):
        """Returns the max possible path-length from a given node
        :type node: TreeNode
        :rtype: int
        """

        if not node:
            return 0
        depth_left = self.depth(node.left)
        depth_right = self.depth(node.right)
        self.ans = max(self.ans, depth_left + depth_right + 1)
        return max(depth_left, depth_right) + 1


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)

    sol = Solution()
    print(sol.diameterOfBinaryTree(node))  # 3
