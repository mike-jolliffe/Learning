class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        perm_container = [S]
        S = list(S)

        def swap_case(ix, string):
            """Return versions of the string with ix uppercased and lowercased"""
            s_up = string[:]
            s_dn = string[:]
            try:
                if string[ix].isalpha():
                    s_up[ix] = s_up[ix].upper()
                    s_dn[ix] = s_dn[ix].lower()
                    perm_container.extend([''.join(s_up), ''.join(s_dn)])
                return swap_case(ix+1, s_up), swap_case(ix+1, s_dn)
            except IndexError:
                return None
        # Run swap_case for all indexes
        swap_case(0, S)
        # Reduce container to unique permutations
        return list(set(perm_container))


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCasePermutation("A12b3cD"))  # should be 2^4 unique permutations
