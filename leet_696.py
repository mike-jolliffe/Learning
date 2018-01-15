class Solution:
    def countBinarySubstrings(self, s):
        """Returns the number of non-empty substrings in s that have the same
           number of 0s and 1s, where all 0s and 1s are grouped consecutively.
        :type s: str
        :rtype: int
        """

        num_substrings = 0
        substrings = []

        for ix, val in enumerate(s):
            length, index = self.countTilSwitch(val, s[ix: ])
            next_digit = str(1 - int(val))
            length2, index2 = self.countTilSwitch(next_digit, s[index: ])
            if length2 >= length:
                num_substrings += 1
                substrings.append(s[ix:(index+index2)])

        print(substrings)
        return num_substrings

    def countTilSwitch(self, start, substring):
        """Returns the length of string before digits switch, and index of switch
        :type start: str
        :type substring: str
        :rtype: tuple(str, int)
        """

        count = 0
        for ix, val in enumerate(substring):
            # If digit stays same, increment
            if val == start:
                count += 1
            # If digit switches, return count and index of switch
            else:
                print("Digit switches at {}".format(ix))
                return (count, ix)
        return (count, ix)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countBinarySubstrings("00110011"))  # 6
    #print(sol.countTilSwitch("1", "11001"))  # (2, 2)
