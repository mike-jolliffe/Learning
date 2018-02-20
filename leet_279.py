from math import sqrt

class Solution:
    def numSquares(self, n):
        """Return minimum number of perfect squares that sum to n
        :type n: int
        :rtype: int
        """

        # First get all perfect squares
        stop = sqrt(n)
        squares_list = self.allSquares(stop)
        #print(squares_list)

        def min_subset(k, s):
            best = s # use all ones
            for i, j in enumerate(squares_list[:k]):
                if j <= s:
                    sz = min_subset(i, s-j)+1
                    if sz < best: best = sz
            return best

        return min_subset(len(squares_list), n)

    def allSquares(self, stop_val):
        """Returns list of all perfect squares up to the stop_val
        :type stop_val: int
        :rtype: List[int]
        """
        all_squares = []
        for i in range(1, int(stop_val) + 1):
            all_squares.append(i ** 2)
        return all_squares

if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(50))
