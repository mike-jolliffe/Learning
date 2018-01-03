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

    def splitOnMax(self, array):
        """Return two subarrays split on index of max val in array
        :type array: List[int]
        :rtype: Dict
        """
        array_dict = {}
        # Get location of max val in list
        max_index = array.index(max(array))
        # Store the max val
        array_dict['Max'] = max(array)
        # Store the left subarray
        array_dict['Left'] = array[0:max_index]
        # Store the right subarray 
        array_dict['Right'] = array[max_index + 1 :]

        return array_dict
