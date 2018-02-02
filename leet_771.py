class Solution:
    def numJewelsInStones(self, J, S):
        """Return number of matches from J in S
        :type J: str
        :type S: str
        :rtype: int
        """

        return len([stone for stone in list(S) if stone in list(J)])

if __name__ == '__main__':
    sol = Solution()
    print(sol.numJewelsInStones("aA", "aAAbbbb"))  # 3
    print(sol.numJewelsInStones("a", "AAbbbb"))  # 0
