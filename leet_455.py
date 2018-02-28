class Solution:
    def findContentChildren(self, g, s):
        """Return the max number of possible child/cookie pairings where s[i] >= g[i],
           meaning child content with cookie
        :type g: List[int] representing greed level of a given child
        :type s: List[int] representing cookie size
        :rtype: int
        """

        contented_children = 0
        # Attempt to assign cookies, starting with greediest child first
        for child in reversed(sorted(g)):
            # Get any possible cookies satisfying greedy child
            can_satisfy = [cookie for cookie in s if cookie >= child]
            # if matches
            if can_satisfy:
                # Tally the contented child
                contented_children += 1
                # Remove the cookie from the pool
                s.remove(can_satisfy[0])
        return contented_children


if __name__ == '__main__':
    sol = Solution()
    print(sol.findContentChildren([1,2], [1,2,3]))  # 2
    print(sol.findContentChildren([1,2,3], [1,1]))  # 1
