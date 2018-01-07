# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def invertTree(self, root):
        """Returns an inverted binary tree (left is right)
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root is None:
            right = self.invertTree(root.right)
            left = self.invertTree(root.left)
            # Invert
            root.left, root.right = right, left
            return root
        else:
            return None

if __name__ == '__main__':
    sol = Solution()
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node1.right = TreeNode(3)
    node1.left.left = TreeNode(4)
    node1.right.left = TreeNode(5)
    node1.right.right = TreeNode(6)
    node1.right.right.right = TreeNode(7)
    inverted = sol.invertTree(node1)
    print([node1, node1.left, node1.right, node1.left.left, node1.left.right,
           node1.right.left, node1.right.right, node1.left.left.left])
