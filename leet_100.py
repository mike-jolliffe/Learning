# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.checked_nodes = []

    def isSameTree(self, p, q):
        """Checks if two binary trees are identical
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.compareNodes(p, q)
        return all(self.checked_nodes)

    def compareNodes(self, p, q):
        """Recursively compares node pairs, stores boolean of comparison in instance
           variable.
        :type p: TreeNode
        :type q: TreeNode
        """
        if p and q:
            if not p.val == q.val:
                self.checked_nodes.append(False)
            return (self.isSameTree(p.left, q.left),
                    self.isSameTree(p.right, q.right))
        elif p is None and q is None:
            self.checked_nodes.append(True)
        else:
            self.checked_nodes.append(False)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node2 = TreeNode(1)
    node2.left = TreeNode(2)
    node3 = TreeNode(1)
    node3.right = TreeNode(2)

    sol = Solution()
    print(sol.isSameTree(node1, node2))  # True
    print(sol.isSameTree(node1, node3))  # False
