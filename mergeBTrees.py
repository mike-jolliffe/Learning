# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.hasChildren = self.hasChildren()

    def __str__(self):
        return str(self.val)

    def hasChildren(self):
        """
        :type node: TreeNode
        :rtype: boolean
        """
        # Check if t1 and t2 have children
        if self.left == None and self.right == None:
            print("no children for this node")
            return False
        else:
            print("node found")
            return True


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        node_vals = []

        if t1 == t2 == None:
            return None
        elif t1 == None:
            if t1.hasChildren == t2.hasChildren == False:
            node_vals.append(t1.val + t2.val)
            return ("Bottom of this branch!")

        elif t1.hasChildren == False:
            node_vals.append(t1.val + t2.val)
            return self.mergeTrees(None, t2.left), self.mergeTrees(None, t2.right)

        elif t2.hasChildren == False:
            node_vals.append(t1.val)
            return self.mergeTrees(t1.left, None), self.mergeTrees(t1.right, None)

        else:
            node_vals.append(t1.val + t2.val)
            return self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right)


    # def addNodes(self, t1, t2):
    #     """
    #     :type t1: TreeNode
    #     :type t2: TreeNode
    #     :rtype: integer
    #     """
    #
    #     if t1.val == None:
    #         print(t1.val)
    #         return t2
    #     elif t2.val == None:
    #         print(t2.val)
    #         return t1
    #     else:
    #         print(t1.val + t2.val)
    #         return TreeNode(t1.val + t2.val)

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
    print(sol.mergeTrees(node1, node2))
