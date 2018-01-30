from collections import defaultdict

class Solution:
    def partitionLabels(self, S):
        """Partitions string into as many substrings as possible, such that any
           given char occurs in only one of the substrings
        :type S: str
        :rtype: List[int]
        """

        start_end_dict = defaultdict(list)
        # For each char in S, get its start/end index
        for ix in range(len(S)):
            start_end_dict[S[ix]].append(ix)
        start_end_dict = {key:[min(value), max(value)] for key,value in start_end_dict.items()}
        print(start_end_dict)

        # Find all clean breaks across start/end indexes so none bridges a substring
        segs = []
        for seg_one in start_end_dict.values():
            x = range(seg_one[0],seg_one[1])
            xs = set(x)
            for seg_two in start_end_dict.values():
                y = range(seg_two[0], seg_two[1])
                if xs.intersection(y):
                    seg_one = [min([seg_one[0], seg_two[0]]), max([seg_one[1], seg_two[1]])]
                    if not seg_one in segs:
                        segs.append(seg_one)
        print(segs)

if __name__ == '__main__':
    sol = Solution()
    sol.partitionLabels('ababcbacadefegdehijhklij')
