class Solution:
    def __init__(self):
        self.validPerms = []
        self.numPairs = 3 #TODO change to None when done testing

    def generateParenthesis(self, n):
        """Generate all possible valid permutations of n pairs of parentheses
        :type n: int
        :rtype: List[str]
        """

        # No nesting
        # One level nesting (single and multiple)
        # Two level nesting (single and multiple)
        # n-1 level nesting

    def nestParens(self, level, n):
        """Given a nesting level, returns all valid permutations for that level
        :type level: int
        :type n: string
        :rtype: None
        """
        if level <= self.numPairs - 1:
            for ix in range(0, len(n) - 1, 2):
                new_n = n
                for jx in range(ix + 1, len(n), 2):
                    print("{}{} -- {}{}".format(ix, jx, n[ix], n[jx]))
                    new_n = new_n[:ix] + self.nest("()", new_n[ix:jx+1]) + new_n[jx+2:]
                    print(new_n)
                    return self.nestParens(level + 1, new_n)
                    break


    def nest(self, a, b):
        """Nests a inside of b
        :type a: string
        :type b: string
        :rtype: string
        """
        # Split string for injection
        midpoint = int(len(b) / 2)
        # Inject a pair of parentheses
        #print("{}{}{}".format(b[:midpoint], a, b[midpoint:]))
        return "{}{}{}".format(b[:midpoint], a, b[midpoint:])

if __name__ == '__main__':
    sol = Solution()
    #print(sol.nest("()", "()"))  # (())
    #print(sol.nest("()", "((()))"))  # (((())))
    sol.nestParens(1, "()()()")  # (())() ()(())
