class Solution:
    def to_binary(self, val):
        """
        :type val: int
        :rtype: string
        """

        binary = ""

        while val > 0:
            binary = str(val % 2) + binary
            val = val // 2

        return binary

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Convert the inputs to str representations of binary
        x_bin = self.to_binary(x)
        y_bin = self.to_binary(y)


        while True:
            if len(x_bin) < len(y_bin):
                x_bin = "0" + x_bin
            elif len(y_bin) < len(x_bin):
                y_bin = "0" + y_bin
            else:
                break

        print(x_bin, y_bin)
        # Placeholder for distance
        dist = 0

        # Pair-wise comparison to calc distance
        for i,j in zip(x_bin, y_bin):
            if i != j:
                dist += 1
        return dist

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingDistance(124,12))
