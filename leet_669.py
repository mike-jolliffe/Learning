# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            # If not a TreeNode
            if not node:
                return None
            # If node is greater than R, throw out all to right
            elif node.val > R:
                return trim(node.left)
            # If node is less than L, throw out all to left
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(0)
    node.right.left = TreeNode(5)
    node.right.right = TreeNode(13)
    sol = Solution()
    print(sol.trimBST(node, 1, 10))
    print(node.left.right)  # None
