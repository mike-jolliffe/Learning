class Solution:
    def countBits(self, num):
        """Return list with count of 1s in each binary num <= given num
        :type num: int
        :rtype: List[int]
        """

        ones_count = []
        for number in range(num + 1):
            ones = [val for val in bin(number) if val == '1']
            ones_count.append(len(ones))
        return ones_count

if __name__ == '__main__':
    sol = Solution()
    print(sol.countBits(5))  # [0,1,1,2,1,2]
