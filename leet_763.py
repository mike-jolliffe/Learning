from collections import defaultdict

class Solution:
    def __init__(self):
        self.intervalList = []

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
        start_end_dict = {key:(min(value), max(value)) for key,value in start_end_dict.items()}

        # Store a list of all start/end indexes
        self.intervalList = list(start_end_dict.values())

        # Reduce overlapping start/end indexes to single encompassing index
        result = self.reduceToExclusive(self.intervalList)
        # Return the length of each substring start/stop, inclusive of stop
        return [len(range(x[0], x[1] + 1)) for x in result]

    def combineIntervals(self, firstInterval, intervalList):
        """Returns a tuple representing full range of combined overlapping
           intervals from list
        :type firstInterval: Tuple
        :type intervalList: List[Tuple]
        :rtype: Tuple
        """

        x = range(firstInterval[0], firstInterval[1] + 1)
        xs = set(x)

        new_start = firstInterval[0]
        new_stop = firstInterval[1]
        wasCombined = 0
        for val in intervalList:
            y = range(val[0], val[1] + 1)
            if xs.intersection(y):
                wasCombined += 1
                temp_start = min([firstInterval[0], val[0]])
                temp_stop = max(firstInterval[1], val[1])
                if temp_start < new_start:
                    new_start = temp_start
                if temp_stop > new_stop:
                    new_stop = temp_stop
                #print(firstInterval, val, (new_start, new_stop))
        return (wasCombined, (new_start, new_stop))

    def reduceToExclusive(self, intervalList):
        """Recursively reduces a List of tuples until none of their ranges overlap
        :type: intervalList: List[Tuple]
        :rtype: List[Tuple]
        """

        new_intervalList = []
        # Keep track of whether reductions are still happening
        total_combined = 0
        for interval in intervalList:
            # For each interval, try reducing by combining with others in List
            wasCombined, result = self.combineIntervals(interval, intervalList)
            if wasCombined > total_combined:
                total_combined = wasCombined
            if not result in new_intervalList:
                # Put the result into a new list
                new_intervalList.append(result)
        # If any combinations beyond with itself happened
        if total_combined > 1:
            # Recursively continue reducing
            return self.reduceToExclusive(new_intervalList)
        else:
            # If no new combinations, return the final list
            return new_intervalList



if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionLabels('ababcbacadefegdehijhklij'))
