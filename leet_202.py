class Solution(object):
    def __init__(self, n):
        self.num_start = n
        self.iters = 0

    def isHappy(self, n):
        """Returns whether squaring a number's digits recursively converges to 1
        (e.g., 19 => 81 (1**2 + 9**2), which becomes 68, then 100, then 1, where
        it stays
        :type n: int
        :rtype: bool for non-recursive base cases
        """
        # if n is one, stop
        if n == 1:
            return True
        # If the chain of numbers starts to repeat, we know non-convergent
        elif n == self.num_start and self.iters > 0:
            return False
        # otherwise,
        else:
            self.iters += 1
            # break number into its digits, square them, then add back together
            n = sum([int(digit) ** 2 for digit in str(n)])
            return self.isHappy(n)


if __name__ == '__main__':
    sol = Solution(19)
    print(sol.isHappy(19))  # True

    sol2 = Solution(4)
    print(sol2.isHappy(4))  # False
