class Solution:
    def findLUSlength(self, a, b):
        """
        Given a group of two strings, finds the longest uncommon
        subsequence of this group of two strings.
        :type a: str
        :type b: str
        :rtype: int
        """

        # Max length tracker
        max_uncommon = 0
        # For sequence start in first string a
        for start in range(len(a)):
            # Length tracker
            curr_length = 1
            # For sequence end in range a+1 till end of a
            for stop in range(start, len(a)):
                # If the sequence is not in b
                if not a[start:stop+1] in b:
                    # Check length tracker against max length
                    curr_length = len(a[start:stop+1])
                    if curr_length > max_uncommon:
                        # Replace max_uncommon if current longer
                        max_uncommon = curr_length
                else:
                    # if substring in b, reset current length to 0
                    curr_length = 0
        # For sequence start in first string b
        for start in range(len(b)):
            # Length tracker
            curr_length = 1
            # For sequence end in range a+1 till end of a
            for stop in range(start, len(b)):
                # If the sequence is not in b
                if not b[start:stop+1] in a:
                    # Check length tracker against max length
                    curr_length = len(b[start:stop+1])
                    if curr_length > max_uncommon:
                        # Replace max_uncommon if current longer
                        max_uncommon = curr_length
                else:
                    # if substring in b, reset current length to 0
                    curr_length = 0
        # return max length tracker if max length tracker > 0 else -1
        return max_uncommon if max_uncommon > 0 else -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.findLUSlength("abcd", "abcd"))  # -1
    print(sol.findLUSlength("aba", "cdc"))  # 3
    print(sol.findLUSlength("abc", "abcd"))  # 1
