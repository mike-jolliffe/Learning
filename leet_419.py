class Solution:
    def countBattleships(self, board):
        """Return number of battleships on a board
        :type board: List[List[str]]
        :rtype: int
        """

        ship_count = 0
        # Search through board until you find an X, add to xydict.
        X_list = self.toXYList(board)
        print(X_list)

        # Search from X in all four directions recursively, changing Xs to Os
        while X_list:
            start = X_list.pop()
            adjacent = self.getAdjacent(X_list, start)
            #print("Adjacent to {} -- {}".format(start, adjacent))
            #print("Full list right now: {}".format(X_list))
            ship_count += 1

        return ship_count

    def toXYList(self, board):
        """Returns list of xy locations for all Xs
        :type board: List[List[str]]
        :rtype: List[tuple]
        """
        Xs = []
        for row_ix in range(len(board)):
            for col_ix in range(len(board[0])):
                if board[row_ix][col_ix] == 'X':
                    Xs.append((col_ix, row_ix))
        return Xs

    def getAdjacent(self, loc_list, starting_location, adjacents=[]):
        """Returns xy_value of all adjacent Xs
        :type loc_list: List[tuple]
        :type starting_location: tuple
        :type adjacents: List[tuple]
        :rtype: List[tuple]
        """
        four_dirs = [(starting_location[0] - 1, starting_location[1]),
                     (starting_location[0], starting_location[1] - 1),
                     (starting_location[0] + 1, starting_location[1]),
                     (starting_location[0], starting_location[1] + 1)]


        for loc in loc_list:
            if loc in four_dirs:
                adjacents.append(loc)
                loc_list.remove(loc)
                return self.getAdjacent(loc_list, loc, adjacents)
        return adjacents

if __name__ == '__main__':
    sol = Solution()
    print(sol.countBattleships([['.','.','.','X'],['.','X','.','X'],
                  ['.','X','.','X']]))  # 2
