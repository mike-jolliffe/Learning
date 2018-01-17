class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.treeList = []

    def findTarget(self, root, k):
        """Check whether k can be created by the sum of any two nodes
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # Convert btree to a List object
        self.treeToList(root)

        for i in range(len(self.treeList) - 1):
            for j in range(i+1, len(self.treeList)):
                if self.treeList[i] + self.treeList[j] == k:
                    return True
        return False

    def treeToList(self, root):
        """Converts btree into a list of node vals
        :type root: TreeNode
        :type treeList: List[int]
        :rtype: List[int]
        """

        # Base case, root is None
        if root is None:
            return None
        else:
            self.treeList.append(root.val)
            return self.treeToList(root.left), self.treeToList(root.right)


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.right.right = TreeNode(7)

    sol = Solution()
    print(sol.findTarget(node, 11))  # True
    print(sol.findTarget(node, 12))  # False
