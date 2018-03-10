class Solution(object):
    def checkRecord(self, s):
        """Check string for more than 2 A's or an 'LLL'
        :type s: str
        :rtype: bool
        """
        # Three consecutive Ls, return False
        if 'LLL' in s:
            return False
        # If more than one A occurs, return False
        elif len([char for char in s if char == 'A']) > 1:
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkRecord('ADDBDBLLA'))  # False b/c of A
    print(sol.checkRecord('ADDBDBLLL'))  # False b/c of L
    print(sol.checkRecord('ADDBDBLL'))  # True
