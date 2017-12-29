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
        # For sequence start in first string a
            # For sequence end in range a+1 till end of a
                # Length tracker
                # If the sequence is not in b
                    # Check length tracker against max length
        # return max length tracker if max length tracker > 0 else -1
