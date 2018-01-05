# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def maxDepth(self, root, depth=0):
        """Return max depth of btree in number of nodes
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return depth
        return max(self.maxDepth(root.left, depth+1),
                   self.maxDepth(root.right, depth+1))

if __name__ == '__main__':
    sol = Solution()
    node1 = TreeNode(5)
    node1.left = TreeNode(4)
    node1.right = TreeNode(2)
    node1.left.left = TreeNode(3)
    node1.left.left.right = TreeNode(2)
    print(sol.maxDepth(node1))
