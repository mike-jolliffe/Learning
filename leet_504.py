class Solution(object):
    def convertToBase7(self, num):
        """Return base 7 representation of a decimal number
        :type num: int
        :rtype: str
        """

        if num == 0:
            return '0'
        # Starting point - find largest power of 7 that is less than num
        def get_max():
            curr_pow = 0
            while 7 ** curr_pow <= abs(num):
                curr_pow += 1
            return curr_pow - 1

        largest_power = get_max()
        print(largest_power)

        # Create placeholder
        digits = []
        curr_pow = largest_power
        # Descending until number is 0, perform division
        num_div = abs(num)
        while curr_pow >= 0:
            # Get digit value at current power placeholder
            digit = num_div // 7 ** curr_pow
            digits.append(str(digit))
            print(digits)
            try:
                # Return the remainder
                num_div = num_div % (digit * 7 ** curr_pow)
            except ZeroDivisionError:
                pass
            curr_pow -= 1
        # Capture the negative, if exists
        if num < 0:
            digits = ['-'] + digits
        # Flip around so lowest power to the
        return ''.join(digits)


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToBase7(100))  # 202
    print(sol.convertToBase7(-7))  # -10
    print(sol.convertToBase7(-8))  # -11
    print(sol.convertToBase7(0))  # 0
