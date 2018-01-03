class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """ Build binary tree splitting by array max as root
        :type nums: List[int]
        :rtype: TreeNode
        """

        # Split the array by max val and make it a TreeNode
        root_dict = self.splitOnMax(nums)
        if root_dict:
            root = root_dict['Max']

            if root_dict['Left'] == root_dict['Right'] == []:
                return root
            elif root_dict['Left'] == []:
                root.right = self.constructMaximumBinaryTree(root_dict['Right'])
            elif root_dict['Right'] == []:
                root.left = self.constructMaximumBinaryTree(root_dict['Right'])
            else:
                root.left = self.constructMaximumBinaryTree(root_dict['Left'])
                root.right = self.constructMaximumBinaryTree(root_dict['Right'])

    def splitOnMax(self, array):
        """Return two subarrays split on index of max val in array
        :type array: List[int]
        :rtype: Dict
        """
        array_dict = {}
        # Get location of max val in list
        if len(array) > 0:
            max_index = array.index(max(array))
            # Store the max val
            array_dict['Max'] = TreeNode(max(array))
            # Store the left subarray
            array_dict['Left'] = array[0:max_index]
            # Store the right subarray
            array_dict['Right'] = array[max_index + 1 :]

        return array_dict

if __name__ == '__main__':
    sol = Solution()
    btree = sol.constructMaximumBinaryTree([3,2,1,6,0,5])
    print(btree.val)
