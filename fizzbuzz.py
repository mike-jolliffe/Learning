class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        container = []

        counter = 1
        while counter <= n:
            if counter % 3 == 0 and counter % 5 == 0:
                container.append("FizzBuzz")
            elif counter % 5 == 0:
                container.append("Buzz")
            elif counter % 3 == 0:
                container.append("Fizz")
            else:
                container.append(str(counter))
            counter += 1

        return container

if __name__ == '__main__':
    sol = Solution()
    print(sol.fizzBuzz(15))
