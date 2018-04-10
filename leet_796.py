class Solution(object):
    def rotateString(self, A, B):
        """Check if shifting A an arbitrary number of times could result in B
        :type A: str
        :type B: str
        :rtype: bool
        """
        shifts = 0
        while shifts < len(A):
            # create string by moving front element to back
            A = A[1:] + A[0]
            if A == B:
                return True
            shifts += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.rotateString('abcde', 'cdeab'))  # true
    print(sol.rotateString('abcde', 'cdaeb'))  # false
