# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Create level counter
    current_level = 1
    # Create dictionary w/key as level, vals as vals
    level_dict = {}

    def averageOfLevels(self, root):
        """
        Return the average of values at each level of binary tree
        :type root: TreeNode
        :rtype: List[float]
        """
        # Build dict for tracking level values
        self.build_leveldict(root)

        # Create list for holding level avgs
        level_avgs = []

        for level in self.level_dict.values():
            # Calculate the average for each level's values
            total = sum(level)
            level_avgs.append(total / float(len(level)))

        return level_avgs

    def build_leveldict(self, root):
        """
        Return dictionary of values by btree level
        :type root: TreeNode
        :rtype: Dict[int]
        """

        # if self.val is None, you are at a leaf node
        if root == None:
            return None
        else:
            self.level_dict.setdefault(self.current_level // 2, []).append(root.val)
            self.current_level += 1
            return self.averageOfLevels(root.left), self.averageOfLevels(root.right)

if __name__ == '__main__':
    node1 = TreeNode(3)
    node1.right = TreeNode(20)
    node1.left = TreeNode(9)
    node1.right.left = TreeNode(15)
    node1.right.right = TreeNode(7)
    sol = Solution()
    print(sol.averageOfLevels(node1))
