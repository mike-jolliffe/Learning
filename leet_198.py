class TreeNode:
    next_id = 1

    def __init__(self, x):
        self.id = TreeNode.next_id
        self.val = x
        self.left = None
        self.right = None
        TreeNode.next_id += 1

    def __repr__(self):
        return str(self.val)


class Solution:
    def __init__(self):
        self.root = None

    def rob(self, nums):
        """Given array of nums, return max possible by selecting only non-adjacent
           nums
        :type nums: List[int]
        :rtype: int
        """

        # Initialize the binary tree root as zero
        self.root = TreeNode(0)
        # Build the binary tree from the root
        self.toBinaryTree(nums, self.root)
        print([self.root.left, self.root.right, self.root.left.left,
               self.root.left.right, self.root.right.left, self.root.right.right])

    # Make binary tree of possible routes. Include unique id
    def toBinaryTree(self, numsArray, newNode):
        """Convert array into binary tree split by move of two or three after
           initial split on first or second element
        :type numsArray: List[int]
        :type newNode: TreeNode
        :rtype: None
        """

        if numsArray:
            try:
                newNode.left = TreeNode(numsArray[0])
                newNode.right = TreeNode(numsArray[1])
                # Move up two places in the array, start from left node
                return (self.toBinaryTree(numsArray[2:], newNode.left),
                # Move up three places in the array, start from right node
                self.toBinaryTree(numsArray[3:], newNode.right))
            except:
                pass
        else:
            return self.root

    # # Memoize sums by unique id
    # def memoize(f):
    #     memo = {}
    #     def helper(x):
    #         if x not in memo:
    #             memo[x] = f(x)
    #         return memo[x]
    #     return helper
    #
    # @memoize
    # # Traverse binary tree, getting max of all sums

# print(fib(40))


if __name__ == '__main__':
    sol = Solution()
    sol.rob([5,2,3,6,3,4,7,5,3,1,2,6])  # 27 (5,6,4,5,1,6)
    sol.rob([5,2,3,6,3,2,7,2,1,8,3,4,7,2,3])  # 36 (5,6,7,8,7)
