class Solution:
    def countBinarySubstrings(self, s):
        """Returns the number of non-empty substrings in s that have the same
           number of 0s and 1s, where all 0s and 1s are grouped consecutively.
        :type s: str
        :rtype: int
        """

        num_strings = 0
        lengths = self.countTilSwitch(s[0], s)
        for i in range(len(lengths) - 1):
            for j in range(i + 1, len(lengths)):
                num_strings += min([lengths[i], lengths[j]])
                break
        return num_strings


    def countTilSwitch(self, start, string):
        """Returns list of lengths between digit switches
        :type start: str
        :type string: str
        :rtype: List[int]
        """
        lengths = []
        count = 0
        for val in string:
            # If digit stays same, increment
            if val == start:
                count += 1
            # If digit switches, return count and index of switch
            else:
                lengths.append(count)
                count = 1
                start = str(1 - int(start))
        lengths.append(count)
        return lengths

if __name__ == '__main__':
    sol = Solution()
    #print(sol.countTilSwitch("0", "00110011"))  # [2,2,2,2]
    print(sol.countBinarySubstrings("00110011"))  # 6
    print(sol.countBinarySubstrings("10101"))  # 4
