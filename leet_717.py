class Solution:
    def isOneBitCharacter(self, bits):
        """Check whether last bit is a single bit character
        :type bits: List[int]
        :rtype: bool
        """
        # set a counter
        i = 0
        # Keep track of jumps
        jumps = []
        while i < len(bits):
            # if first digit in pair is a 1
            if bits[i] == 1:
                # skip over the next digit and repeat
                i += 2
                jumps.append(2)
            # else don't skip over next digit
            else:
                i += 1
                jumps.append(1)
        # check last jump to see if 1 or 2
        return True if jumps[-1] == 1 else False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isOneBitCharacter([1,0,1,0,0]))
    print(sol.isOneBitCharacter([1,0,1,0,1,1,1,0]))
    print(sol.isOneBitCharacter([1,1,1,0]))
