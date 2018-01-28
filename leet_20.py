class Solution:
    def isValid(self, s):
        """Given a string of only parentheses, brackets, and braces, return whether they
           properly open and close in the correct order
        :type s: str
        :rtype: bool
        """

        # Create a stack holding opening types
        openers = []

        pairs = {'(': ')',
                 '{': '}',
                 '[': ']'}

        for bracket in s:
            if bracket in pairs.keys():
                openers.append(bracket)
            else:
                try:
                    last_opener = openers.pop()
                except:
                    return False
                if not pairs[last_opener] == bracket:
                    return False
        # if openers is empty, return True, else False
        return not openers

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("(({[()]}))"))  # True
    print(sol.isValid("(({[()]}))["))  # False
