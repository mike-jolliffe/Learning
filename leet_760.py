class Solution:
    def anagramMappings(self, A, B):
        """Return indexes of values in B ordered by A occurrence
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        return [B.index(num) for num in A]


if __name__ == '__main__':
    sol = Solution()
    print(sol.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))  # [1,4,3,2,0]
