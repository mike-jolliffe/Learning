class Solution:
    def __init__(self):
        # Create dict to hold indexes of local minima and maxima
        self.pv = {"peaks": [], "valleys": []}
        # Keep track of profit
        self.profit = 0
        # Keep track of last price paid
        self.lastPaid = None

    def maxProfit(self, prices):
        """Calculate max possible profit from timing stock market trades
        :type prices: List[int]
        :rtype: int
        """

        # Given a particular price, look ahead until peak or valley
        self.findPVs(prices)
        # Set lastPaid as first value
        self.lastPaid = prices[0]

        # Track type of last transaction
        justBought = None
        # Iterate through daily prices
        for today_ix in range(len(prices)):
            # If the price is a peak and justBought is True or first trans, sell
            if today_ix in self.pv["peaks"] and justBought in [True, None]:
                # SELL, where profit is current price minus last price paid
                self.profit += (prices[today_ix] - self.lastPaid)
                # flip the flag
                justBought = False
            # If price is a valley and not justBought is False or first trans, buy
            elif today_ix in self.pv["valleys"] and justBought in [False, None]:
                # BUY, where lastPaid is updated to current price
                self.lastPaid = prices[today_ix]
                # flip the flag
                justBought = True
        return self.profit


    def findPVs(self, prices, ix = 0):
        """Finds the indexes of local peaks and valleys
        :type ix: int
        :type prices: List[int]
        :rtype: None
        """

        if ix == 0:
            return self.findPVs(prices, ix + 1)
        try:
            # If node is greater than preceding and succeeding vals
            if prices[ix] >= prices[ix - 1] and prices[ix] >= prices[ix + 1]:
                self.pv["peaks"].append(ix)
                print("Local peak: {}".format(ix))
            # If node is less than preceding and succeeding vals
            elif prices[ix] <= prices[ix - 1] and prices[ix] <= prices[ix + 1]:
                self.pv["valleys"].append(ix)
                print("Local valley: {}".format(ix))
            # If node not a peak or valley
            else:
                pass
            return self.findPVs(prices, ix + 1)
        except:
            pass

if __name__ == '__main__':
    prices = [1,2,2,1,0,1,3,2,1,1,2]  # {'peaks':[1,2,6], 'valleys':[4,8,9]}
    sol = Solution()
    print(sol.maxProfit(prices))  # 4
