class Solution:
    def maxProfit(self, prices):
        """Returns max profit from array of daily stock prices, where buy and
           sell must happen
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0

        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                trans = prices[j] - prices[i]
                if trans > max_profit:
                    max_profit = trans
        return max_profit

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))  # 5
    print(sol.maxProfit([7,6,4,3,1]))  # 0
