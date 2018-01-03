class Solution:
    def hasAlternatingBits(self, n):
        """ Determines whether a given number has alternating bit values, (e.g.,
            5 => True (101), 6 => False (110))
        :type n: int
        :rtype: bool
        """

        # Convert input integer to binary representation
        binary = "{0:b}".format(n)
        print(binary)

        # Get the first digit
        for i in range(len(binary) - 1):
            # Get its neighbor
            for j in range(i + 1, len(binary)):
                # If neighboring digits same
                print(binary[i], binary[j])
                if binary[i] == binary[j]:
                    return False
                else:
                    break
        # If no neighboring digits same
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.hasAlternatingBits(5))  # True
    print(sol.hasAlternatingBits(6))  # False
