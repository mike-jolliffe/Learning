class Solution:
    def combinationSum(self, candidates, target):
        """Find all combinations of numbers in list that sum to target
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort(reverse=True)
        solutions = []

        def adder(total, nums, ix):
            """Recursively add until match target or run out of numbers"""
            print(f"Total: {total}, target: {target}")
            if total == target:
                return nums
            elif total < target:
                if total + candidates[ix] == target:
                    nums.append(candidates[ix])
                    return nums
                elif total + candidates[ix] <= target - candidates[-1]:
                    nums.append(candidates[ix])
                    return adder(sum(nums), nums, ix)
                elif total + candidates[ix] > target - candidates[-1]:
                    try:
                        return adder(sum(nums), nums, ix + 1)
                    except IndexError:
                        return None

        for index, val in enumerate(candidates):
            result = adder(0, [], index)
            print(result)
            if result and result not in solutions:
                solutions.append(result)
        return solutions


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))  # [[7], [3,2,2]]
    print(sol.combinationSum([2,3,5], 8))  # [[5,3],[3,3,2],[2,2,2,2]]
    print(sol.combinationSum([1,2], 4))  # [[5,3],[3,3,2],[2,2,2,2]]
