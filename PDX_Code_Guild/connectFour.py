import collections

class GameBoard():
    '''creates a connect four game board object'''

    board = {1: [], 2: [], 3: [], 4: [],
             5: [], 6: [], 7: []}
    players = {1: "X", 2: "O"}

    def __init__(self):
        self.connections = 0
        self.last_i = 0
        self.last_j = 0

    def addPiece(self, player, column):
        if len(self.board[column]) < 6:
            self.board[column].append(self.players[player])
            self.last_i = column
            self.last_j = len(self.board[column]) - 1
        else:
            return f'sorry, that column is full!'

    def printBoard(self):
        row_num = 6
        while row_num >= 0:
            row = []
            for index in range(1,8):
                try:
                    row.append("[" + self.board[index][row_num] + "]")
                except:
                    row.append("[ ]")
            print(' '.join(row))
            row_num -= 1

    def checkWin(self):
        horiz_r_i = 1
        horiz_r_j = 0
        horiz_l_i = -1
        horiz_l_j = 0
        vert_i = 0
        vert_j = -1
        diag_l_i = -1
        diag_l_j = -1
        diag_r_i = 1
        diag_r_j = -1


        self.WinDir(self.last_i, self.last_j, horiz_r_i, horiz_r_j, 1)
        if self.connections == 4:
            return True
        else:
            self.connections = 0

        self.WinDir(self.last_i, self.last_j, horiz_l_i, horiz_l_j, 1)
        if self.connections == 4:
            return True
        else:
            self.connections = 0

        self.WinDir(self.last_i, self.last_j, vert_i, vert_j, 1)
        if self.connections == 4:
            return True
        else:
            self.connections = 0

        self.WinDir(self.last_i, self.last_j, diag_l_i, diag_l_j, 1)
        if self.connections == 4:
            return True
        else:
            self.connections = 0

        self.WinDir(self.last_i, self.last_j, diag_r_i, diag_r_j, 1)
        if self.connections == 4:
            return True
        else:
            self.connections = 0
            return False

    def WinDir(self, i, j, i_dir, j_dir, player):

        try:
            while i >= 0 and j >= 0:
                if self.board[i][j] != self.players[player]:
                    return self.connections
                else:
                    self.connections += 1
                    return self.WinDir(i+i_dir, j+j_dir, i_dir, j_dir, player)
        except:
            return self.connections

new_game = GameBoard()
while new_game.connections < 4:
     P1 = input("Pick a location: ")
     new_game.addPiece(1, int(P1))
     new_game.printBoard()
     print()
     print()
     print(new_game.last_i, new_game.last_j)
     print(new_game.checkWin())

#     if new_game.checkWin():
#         print ("winner!")
#         exit()

# # read sample moves file
# file = open('connect-four-moves.txt', 'r')
# print (file.read())
