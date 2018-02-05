# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.distances = {}

    def diameterOfBinaryTree(self, root):
        """Return max number of edges to get from any node to another
        :type root: TreeNode
        :rtype: int
        """

    def traverseTree(self, root):
        """Move through the binary tree, getting distance to leaves from each node
        :type root: TreeNode
        :rtype: None
        """

        if root:
            self.getBranchDistances(root.val, root.left, 1)
            self.getBranchDistances(root.val, root.right, 1)
            return (self.traverseTree(root.left),
                    self.traverseTree(root.right))

    def getBranchDistances(self, parent, root, distance):
        """Calculate the distance between a given root and all same-branch leaves
        :type parent: TreeNode.val
        :type root: TreeNode
        :type distance: int
        :rtype: None
        """

        if root:
            self.distances[(parent, root.val)] = distance
            return (self.getBranchDistances(parent, root.left, distance + 1),
                    self.getBranchDistances(parent, root.right, distance + 1))

    def getMaxDistance(self):
        """Calculates the maximum travel distance in the tree
        :rtype: int
        """
        pass

    # Calculate max distance by combining longest paths that contain a same
        # starting node
if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)

    sol = Solution()
    sol.traverseTree(node)
    print(sol.getMaxDistance())  # 3
