class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def __init__(self):
        self.node_vals = []

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
            elif root_dict['Right'] == []:
                root.left = self.constructMaximumBinaryTree(root_dict['Left'])
            elif root_dict['Left'] == []:
                root.right = self.constructMaximumBinaryTree(root_dict['Right'])
            else:
                root.left = self.constructMaximumBinaryTree(root_dict['Left'])
                root.right = self.constructMaximumBinaryTree(root_dict['Right'])
            return root

    def toConsole(self, nodes):
        """
        :type nodes: List[TreeNode]
        :rtype: List
        """
        new_nodes = []
        for val in nodes:
            if not val == None:
                self.node_vals.append(val.val)
                if not (val.left == None and val.right == None):
                    new_nodes.append(val.left)
                    new_nodes.append(val.right)
            else:
                self.node_vals.append('null')
        if len(new_nodes) > 0:
            return self.toConsole(new_nodes)
        else:
            return self.node_vals

    def splitOnMax(self, array):
        """Return two subarrays split on index of max val in array
        :type array: List[int]
        :rtype: Dict
        """
        array_dict = {}
        # Get location of max val in list
        if len(array) > 1:
            max_index = array.index(max(array))
            # Store the max val
            array_dict['Max'] = TreeNode(max(array))
            # Store the left subarray
            array_dict['Left'] = array[0:max_index]
            # Store the right subarray
            array_dict['Right'] = array[max_index + 1 :]
        elif len(array) > 0:
            array_dict['Max'] = TreeNode(array[0])
            array_dict['Left'] = []
            array_dict['Right'] = []

        print("Left array: {} -- Right array: {}".format(array_dict['Left'],
                                                         array_dict['Right']))
        return array_dict

if __name__ == '__main__':
    sol = Solution()
    root = sol.constructMaximumBinaryTree([3,2,1,6,0,5])
    # print([root.val, root.left.val, root.right.val, root.left.left, root.left.right.val])
    print(sol.toConsole([root]))  # [6,3,5,null,2,0,null,null,1]
