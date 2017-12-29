class Solution:
    def canWinNim(self, n):
        """ Determines whether it's possible for first player to win a two-player game
            where player can take 1-3 stones, and player taking last stone wins
        :type n: int
        :rtype: bool
        """

        if n % 4 == 0:
            return False
        else:
            return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.canWinNim(1))  # True
    print(sol.canWinNim(3))  # True
    print(sol.canWinNim(4))  # False
    print(sol.canWinNim(5))  # True
    print(sol.canWinNim(7))  # True
