class Solution:
    def climbStairs(self, n):
        """Returns total possible permutations to reach n using fibonacci approach
        :type n: int
        :rtype: int
        """

        a = b = 1
        for i in range(n - 1):
            temp = a + b
            a = b
            b = temp
        return b

    def climbStairsRecursive(self, n):
        """Solves fibonacci sequence problem using recursion"""
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairsRecursive(n-1) + self.climbStairsRecursive(n-2)

if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(4))  # 5
    print(sol.climbStairs(5))  # 8

    print(sol.climbStairsRecursive(4))  # 5
    print(sol.climbStairsRecursive(5))  # 8
