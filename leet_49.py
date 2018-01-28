class Solution:
    def groupAnagrams(self, strs):
        """Groups anagrams together
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        grouped = []
        # If string not empty, put first anagram in its own list
        if strs:
            grouped.append([strs.pop(0)])
            # For each anagram, if doesn't match existing list, put in own list
            for anagram in strs:
                # Flag for catching stand-alone/first instances of anagrams
                hasGroup = False
                # Compare anagram to existing list of lists
                for group in grouped:
                    #print((anagram, group[0], self.areAnagrams(anagram, group[0])))
                    # If anagram matches a particular group, append it
                    if self.areAnagrams(anagram, group[0]):
                        group.append(anagram)
                        # Switch flag to true, anagram has existing group
                        hasGroup = True
                        break
                # If no anagram matches, give its own list
                if not hasGroup:
                    grouped.append([anagram])

        # return the grouped anagrams
        return grouped

    def areAnagrams(self, A1, A2):
        """Compares to strings to check if anagrams
        :type A1: string
        :type A2: string
        :rtype: boolean
        """

        # Check no excess letters in one or other
        if len(A1) == len(A2):
            for char in A1:
                if not char in A2:
                    return False
                else:
                    A2 = A2.replace(char, '', 1)
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.areAnagrams("ate", "eat"))  # True
    print(sol.areAnagrams("ate", "nat"))  # False
    print(sol.areAnagrams("owl", "woo"))  # False
    print(sol.areAnagrams("ate", "eeat"))  # False
    print(sol.areAnagrams("pup", "yup"))  # False

    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'],['tan', 'nat'],['bat']]
