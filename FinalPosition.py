class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Track x and y position
        x_pos = 0
        y_pos = 0

        for move in moves:
            if move == "U":
                y_pos += 1
            elif move == "D":
                y_pos -= 1
            elif move == "R":
                x_pos += 1
            elif move == "L":
                x_pos -= 1

        return True if x_pos == 0 and y_pos == 0 else False

if __name__ == "__main__":
    sol = Solution()
    print(sol.judgeCircle("UDDLRU"))
    print(sol.judgeCircle("DDRRRR"))
