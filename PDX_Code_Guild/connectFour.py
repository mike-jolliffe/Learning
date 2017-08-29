import collections

class GameBoard():
    '''creates a connect four game board object'''

    board = collections.OrderedDict({1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []})
    players = {1: "X", 2: "O"}

    vert = [board[i][i], board[i][i+1], board[i][i+2], board[i][i+3]]
    horiz = [board[i][i], board[i+1][i], board[i+2][i], board[i+3][i]]
    diag_up = [board[i][i], board[i+1][i+1], board[i+2][i+2], board[i+3][i+3]]
    diag_down = [board[i][i], board[i-1][i-1], board[i-2][i-2], board[i-3][i-3]]

    def addPiece(self, player, column):
        if len(self.board[column]) < 6:
            self.board[column].append(self.players[player])
        else:
            return f'sorry, that column is full!'

    def printBoard(self):
        [print(x) for x in self.board.values()]

    def checkWin(self, player, column):
        connect_count = 0
        connections = True
        start = self.board[column][-1]
        while connections:
            # look immediately around the most recent play
            if self.board[column][start - 1] == players[player]:
                connect_count += 1


            # if there a player of same type, recursively look around that one


# # read sample moves file
# file = open('connect-four-moves.txt', 'r')
# print (file.read())

new_game = GameBoard()
new_game.addPiece(1,1)
new_game.printBoard()

