# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.levels_dict = {}

    def largestValues(self, root):
        """Returns largest value in each level of binary tree
        :type root: TreeNode
        :rtype: List[int]
        """
        # Make dictionary of all values by level
        self.toLevelsDict(root)

        # For each level, grab the max
        return [max(val) for key, val in self.levels_dict.items()]

    def toLevelsDict(self, root, level=1):
        """Puts all values into dictionary with levels as key
        :type root: TreeNode
        :type level: int
        :rtype: None
        """

        if root:
            # Append to an existing level, or create new one
            self.levels_dict.setdefault(level,[]).append(root.val)
            return (self.toLevelsDict(root.left, level + 1),
                    self.toLevelsDict(root.right, level + 1))


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(7)


    sol = Solution()
    print(sol.largestValues(node))  # [1,3,7]
