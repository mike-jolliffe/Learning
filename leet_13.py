class Solution:
    def __init__(self):
        self.romans_dict = {'I': 1, 'V': 5, 'X': 10,
                       'L': 50, 'C': 100, 'D': 500,
                       'M': 1000}
        self.partsList = []

    def romanToInt(self, s):
        """Convert roman numerals to int
        :type s: str
        :rtype: int
        """

        # Break romans into individual vals
        self.romanToParts(s, ['V', 'X', 'L', 'C', 'D', 'M'])

        # Move through partsList, adding values
        total = 0
        for val in self.partsList:
            if len(val) == 2:
                total += (self.romans_dict[val[1]] - self.romans_dict[val[0]])
            else:
                total += self.romans_dict[val]
        return total

    def romanToParts(self, s, demarc):
        """Breaks string into associated values
        :type s: str
        :type demarc: List[str]
        :rtype: List[str]
        """
        if demarc:
            current_demarc = demarc.pop()
            if s:
                for i in range(len(s)):
                    #print("current ix: {}, length: {}".format(i, len(s)))
                    if s[i] == current_demarc:
                        try:
                            self.partsList.append("{}{}".format(s[i - 1], s[i]))
                            # Remove both from string
                            new_i = max([i - 2, 0])
                            s = s[:new_i] + s[i + 1:]
                            #print("{} -- {}".format(self.partsList, s))
                            break
                        except:
                            self.partsList.append(s[i])
                            # Remove just s[i] from string
                            s = s[:i] + s[i + 1:]
                            #print("{} -- {}".format(self.partsList, s))
                            break
            return self.romanToParts(s, demarc)

if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("XCIX"))  # 99
