class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        # Create instance variable to hold final ordered node values
        self.bfs = []

    def bfsTraversal(self, root):
        """Return all nodes of graph in order using BFS left-to-right
        :type root: TreeNode
        :rtype: List[int]
        """
        # keep track of nodes to be checked
        current_level = [root]

        while current_level:
            # Create holder for child nodes
            next_level = []
            # For each node in current-level queue
            for n in current_level:
                if n is None:
                    self.bfs.append(n)
                else:
                    # Append that node value to the instance variable
                    self.bfs.append(n.val)
                    next_level.append(n.left)
                    next_level.append(n.right)
            # Reset the queue to be the child nodes
            current_level = next_level

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.right = TreeNode(3)

    sol = Solution()
    sol.bfsTraversal(node)
    print(sol.bfs)  # [1,2,None,None,3,None,None]
