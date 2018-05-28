class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = A[:]
        for i in range(len(A)):
            for j in range(len(A[i])):
                B[i][j] = abs(1-A[i][j])
            B[i].reverse()
        return B


if __name__ == '__main__':
    sol = Solution()
    print(sol.flipAndInvertImage([[1,0,0,1],[1,1,0,0]]))  # [[0,1,1,0],[0,0,1,1]]
