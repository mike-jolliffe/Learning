class Room(object):
    '''Used to generate a room for moving, fighting, exploring'''
    def __init__(self, size, difficulty, entrance, room_exit):
        self.size = size
        self.difficulty = difficulty
        self.entrance = entrance
        self.room_exit = room_exit

    def print_Room(self):
        row_num = self.size[0] - 1
        while row_num >= 0:
            row = []
            for index in range(self.size[1]):
                try:
                    # TODO fix this for placing Hero, Creatures, Items
                    row.append("[" + self.board[index][row_num] + "]")
                except:
                    row.append(" . ")
            print(' '.join(row))
            row_num -= 1

new_room = Room((7,3), "hard", (0,0), (7,2))
new_room.print_Room()