class Solution:

    def findCircleNum(self, M):
        """Find number of unconnected networks. Connected if directly or
           transtively share i,j (i.e., if 0 and 2 share 1, 0-2 connected).
        :type M: List[List[int]]
        :rtype: int
        """

        # Get direct connections for each member
        membership = self.getMembershipDirect(M)
        #print(membership)
        # Get all direct/indirect connections
        indirect = self.getMembershipIndirect(membership)
        #print(indirect)
        # Count num of distinct groups (i.e., unique relationship sets)
        count = 0
        for i in set(indirect):
            count += 1
        return count

    def getMembershipDirect(self, M):
        """Returns dictionary showing direct connections for each element
        :type M: List[List[1 or 0]]
        :rtype: Dictionary
        """
        # Get direct connections for each node
        groups_dict = {}
        for i, node in enumerate(M):
            groups_dict[i] = [j for j, val in enumerate(node) if val == 1]
        return groups_dict

    def getMembershipIndirect(self, groups_dict):
        """Returns List representing direct and indirect connections for each
           element
        :type: groups_dict: Dictionary
        :rtype: List[List[int]]
        """
        all_connections = []
        for node in groups_dict.keys():
            # If node has been captured, add its values to current group
            resultSet = self.getSharedVals(groups_dict[node], groups_dict)
            all_connections.append(resultSet)
        return all_connections

    def getSharedVals(self, nodeVals, groups_dict):
        """Returns list of commonly shared vals
        :type node: int
        :type distinct_groups: Dictionary
        :rtype: Tuple
        """

        new_nodeVals = []
        foundNewVal = False
        # for each nodeval, grab all connections
        for val in nodeVals:
            new_nodeVals.append(val)
            for val2 in groups_dict[val]:
                if not val2 in nodeVals:
                    new_nodeVals.append(val2)
                    foundNewVal = True
        if foundNewVal:
            return self.getSharedVals(new_nodeVals, groups_dict)
        else:
            return tuple(sorted(set(new_nodeVals)))

if __name__ == '__main__':
    sol = Solution()

    #print(sol.getSharedVals([1,2,3], {1:[2,3,4],2:[1],3:[1,5],4:[1,5],5:[3,4]}))  # [1,2,3,4,5]
    #print(sol.getSharedVals([1,2,3], {1:[2,3],2:[1],3:[1],4:[1,5],5:[3,4]}))  # [1,2,3]
    #print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # 2
    #print(sol.findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))  # 1
    #print(sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))  # 1


print(sol.findCircleNum([[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
 [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
 [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
 [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
 [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
 [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
 [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]))  # 3
