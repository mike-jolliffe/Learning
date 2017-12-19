class Solution:
    def findComplement(self, num):
        """
        Returns the complement of a number (101 => 010)
        :type num: int
        :rtype: int
        """

        # Convert int to binary representation
        input_binary = "{0:b}".format(num)
        output_binary = ""
        for digit in input_binary:
            # Flip the 'bit'
            if digit == "1":
                output_binary += "0"
            else:
                output_binary += "1"
        # Convert back to int using binary
        return int(output_binary, 2)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findComplement(1))
