# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        # self.hasChildren = self.hasChildren()

    def __str__(self):
        return str(self.val)


class Solution(object):

    def __init__(self):
        self.node_vals = []

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 == t2 == None:
            return None
        elif t1 == None:
            self.node_vals.append(t2.val)
            return self.mergeTrees(None, t2.left), self.mergeTrees(None, t2.right)
        elif t2 == None:
            self.node_vals.append(t1.val)
            return self.mergeTrees(t1.left, None), self.mergeTrees(t1.right, None)
        else:
            self.node_vals.append(t1.val + t2.val)
            return self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right)

    def toConsole(self):
        return self.node_vals

if __name__ == "__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(5)
    node10 = TreeNode(3)
    node11 = TreeNode(4)
    node20 = TreeNode(8)
    node1.left = node10
    node1.right = node11
    node2.left = node20
    sol = Solution()
    sol.mergeTrees(node1, node2)
    print(sol.node_vals)
