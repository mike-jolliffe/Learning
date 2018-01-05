# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.max_depth = 0
        self.curr_depth = 0

    def maxDepth(self, root):
        """Return max depth of btree in number of nodes
        :type root: TreeNode
        :rtype: int
        """

        # If you hit a terminal node, return depth
        if root == None:
            if self.curr_depth > self.max_depth:
                self.max_depth = self.curr_depth
                self.curr_depth = 0
                return self.max_depth
            else:
                self.curr_depth = 0
                return self.max_depth
        # Otherwise traverse deeper
        else:
            self.curr_depth += 1
            return maxDepth(root.left), maxDepth(root.right)
