class Solution:
    def reconstructQueue(self, people):
        """Return queue sorted according to height given [h,t] for a person
           where h = person's height, and t = # of people in front of person
           that are taller.
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        new_queue = []
        tmp_next = [100,100]
        while people:
            for person in people:
                numTaller = self.getNumTaller(person[0], new_queue)
                if person[1] == numTaller and person[0] < tmp_next[0]:
                    tmp_next = person
            new_queue.append(tmp_next)
            people.remove(tmp_next)
            tmp_next = [100,100]
        return new_queue

    def getNumTaller(self, person_height, new_queue):
        """Given a queue, returns a count of people in line same height or
           taller than a given height
           :type new_queue: List[List[int]]
           :rtype: int
           """
        if not new_queue:
            new_queue = [[0,0]]
        counter = 0
        for person in new_queue:
            if person[0] >= person_height:
                counter += 1
        return counter

if __name__ == '__main__':
    sol = Solution()
    print(sol.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))  # [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
