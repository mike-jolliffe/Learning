class Solution(object):
    def findRestaurant(self, list1, list2):
        """Return common element with least-summing index across two lists
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        # Get the intersection of the two lists
        in_common = set(list1).intersection(list2)

        # Make index placeholder
        min_word = []
        # Initialize minimum value at infinity
        min_val = float('inf')
        # For all common words
        for word in in_common:
            # Add the indexes of words in respective lists
            index_sum = list1.index(word) + list2.index(word)
            # If that sum is smaller than current minimum, replace
            if index_sum <= min_val:
                # Keep track of current minimum word and its sum
                min_word.append([word, index_sum])
                min_val = index_sum

        # Return the lowest-summing word(s)
        return [word[0] for word in min_word if word[1] == min([word[1] for word in min_word])]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                             ["KFC", "Shogun", "Burger King"]))  # ["Shogun"]
    print(sol.findRestaurant(["Shogun", "KFC", "Tapioca Express", "Burger King"],
                             ["KFC", "Shogun", "Burger King"]))  # [Shogun", "KFC"]
    print(sol.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
                             ["KFC","Burger King","Tapioca Express","Shogun"]))  # All elements
