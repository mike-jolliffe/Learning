# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Solution:
    def __init__(self):
        self.nodeDict = {}

    def findBottomLeftValue(self, root):
        """Returns the left-most value in the last level of a bst
        :type root: TreeNode
        :rtype: int
        """
        self.toXYDict(root)
        # Narrow the node dictionary to only last level key value pairs
        last_level = {key: value for key, value in self.nodeDict.items() if value[0] == max(val[0] for val in self.nodeDict.values())}
        # Return the left-most key for last-level k:v pairs
        return [key for key, value in last_level.items() if value[1] == max(val[1] for val in last_level.values())][0]

    def toXYDict(self, root, y=0, x=0):
        """Returns a dictionary of depth, net left distance for each node
        :type root: TreeNode
        :type y: int
        :type x: int
        """
        if root:
             self.nodeDict[root.val] = (y,x)
             return (self.toXYDict(root.left, y + 1, x + 1),
                     self.toXYDict(root.right, y + 1, x - 1))

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.right = TreeNode(4)
    node.right.right = TreeNode(5)
    node.right.right.left = TreeNode(6)

    sol = Solution()
    sol.toXYDict(node)
    print(sol.findBottomLeftValue())  # 6
