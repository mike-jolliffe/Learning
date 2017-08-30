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

    def checkWin(self, player):
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


        self.WinDir(self.last_i, self.last_j, horiz_r_i, horiz_r_j, player)
        if self.connections == 4:
            return True
        else:
            self.connections = 0

        self.WinDir(self.last_i, self.last_j, horiz_l_i, horiz_l_j, player)
        if self.connections == 4:
            return True
        else:
            self.connections = 0

        self.WinDir(self.last_i, self.last_j, vert_i, vert_j, player)
        if self.connections == 4:
            return True
        else:
            self.connections = 0

        self.WinDir(self.last_i, self.last_j, diag_l_i, diag_l_j, player)
        if self.connections == 4:
            return True
        else:
            self.connections = 0

        self.WinDir(self.last_i, self.last_j, diag_r_i, diag_r_j, player)
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

    def playGame(self, player):
        print("WELCOME TO CONNECT FOUR")
        valid_input = False
        while not valid_input:
            try:
                play = int(input(f"Player {player}, pick a column: "))
                self.addPiece(player, play)
                valid_input = True
            except:
                print("Please enter a number 1 through 7")
                print()
                continue
        self.printBoard()
        if self.checkWin(player):
            print(f"Player {player} wins!!!")
            exit()


if __name__=='__main__':
    connect_four = GameBoard()
    plays = 0
    while plays < 43:
        plays += 1
        connect_four.playGame(1)
        connect_four.playGame(2)
    print(f"Scratch game. Nobody wins!")


