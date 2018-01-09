class Solution:
    def addDigits(self, num):
        """Add digits of number until only one digit remains
        :type num: int
        :rtype: int
        """

        def sumNum(number):
            """Splits number and adds digits
            :type number: int
            :rtype: int"""

            return sum([int(digit) for digit in str(number)])

        # Perform addition until length is 1
        while True:
            if len(str(num)) == 1:
                return num
            else:
                num = sumNum(num)

if __name__ == '__main__':
    sol = Solution()
    print(sol.addDigits(38))  # 2
