class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        # Create total_score placeholder
        total_score = 0
        # Create a round_score list
        round_score = []

        for element in ops:
            # if element is double-digit or negative sign followed by digit
            if len(element) > 1:
                if element.isdigit() or element[1].isdigit():
                    # add element to total_score
                    total_score += int(element)
                    # add element to round_score
                    round_score.append(int(element))
            elif element.isdigit():
                # add element to total_score
                total_score += int(element)
                # add element to round_score
                round_score.append(int(element))
            # if element is "C"
            elif element == 'C':
                # remove last element from round_score
                val = round_score.pop()
                # subtract that element from total_score
                total_score -= val
            # if element is "D"
            elif element == 'D':
                # double last element in round_score
                val = round_score[-1]*2
                # add doubled element to round_score
                round_score.append(val)
                # add doubled element to total_score
                total_score += val
            # if element is plus
            elif element == '+':
                # grab last two elements and add their sum to round_score
                val1 = round_score[-1]
                val2 = round_score[-2]
                round_score.append(val1 + val2)
                # add last two elements to total_score
                total_score += (val1 + val2)
        return total_score

if __name__ == '__main__':
    sol = Solution()
    print(sol.calPoints(["5","2","C","D","+"]))
    print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))
