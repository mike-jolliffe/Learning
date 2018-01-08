class Solution:
    def dailyTemperatures(self, temperatures):
        """Calculates how many days until warmer value observed, if any
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Holds days until warmer for each temp
        days_until = []
        # For start value
        for i in range(len(temperatures) - 1):
            # Create day counter
            count = 0
            # For end value
            for j in range(i + 1, len(temperatures)):
                # Increment counter
                count += 1
                # If end temperature warmer
                if temperatures[j] > temperatures[i]:
                    # Record the count
                    days_until.append(count)
                    # Reset the counter
                    count = 0
                    # Go to next start
                    break
            # Got to end with none greater
            if count > 0:
                count = 0
                days_until.append(0)
        # Append final value, which will always be zero. No next days
        days_until.append(0)
        return days_until

if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
