class Solution:
    def isPowerOfTwo(self, n):
        """Checks whether n is a power of 2
        :type n: int
        :rtype: bool
        """
        while n >= 2:
            n = n / 2
        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(5))  # False
    print(sol.isPowerOfTwo(6))  # False
    print(sol.isPowerOfTwo(1))  # True
    print(sol.isPowerOfTwo(128))  # True
