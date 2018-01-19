# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.node_list = []

    def makevalsArray(self, root):
        """Generates a list of all node values
        :type root: TreeNode
        :rtype: None
        """

        if root is None:
            return None
        else:
            self.node_list.append(root.val)
            return self.makevalsArray(root.left), self.makevalsArray(root.right)

    def buildnewTree(self, root):
        """Converts each node value to sum of itself plus all greater-valued nodes
        :rtype: TreeNode
        """

        # Base case condition
        if root is None:
            return None
        # Otherwise get the sum of value and all greater
        else:
            # Sort the list
            higher_vals = sorted(self.node_list)
            # Sum all values >= root
            root.val = sum(higher_vals[higher_vals.index(root.val):])
            return self.buildnewTree(root.left), self.buildnewTree(root.right)

    def convertBST(self, root):
        """Calls array builder, then builds new tree and returns it
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Build sorted list of node vals
        self.makevalsArray(root)
        # Update the btree values
        self.buildnewTree(root)
        # Return the btree
        return root



if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.right.right = TreeNode(7)

    sol = Solution()
    print(sol.convertBST(node).val)
