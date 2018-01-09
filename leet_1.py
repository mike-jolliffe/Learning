class Solution:
    def twoSum(self, nums, target):
        """Returns from list a sublist of two numbers that sum to target
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Sort nums and chop all vals >= target
        nums2 = sorted(nums)
        # Assign start as smallest number
        for i in range(len(nums2) - 1):
            print(i)
            # Assign end as largest number
            for j in range(len(nums2) - 1, i, -1):
                print("i: {}, j: {}, sum: {}".format(i, j, nums2[i]+nums2[j]))
                # Move end toward start, calculating sum
                if nums2[i] + nums2[j] > target:
                    # If sum greater than target, throw out end
                    nums2.pop()
                # If you hit the sum, return [start, end] values
                elif nums2[i] + nums2[j] == target:
                    first = nums.index(nums2[i])
                    nums.pop(nums.index(nums2[i]))
                    second = nums.index(nums2[j])
                    return [first, second]
        return []

if __name__ == '__main__':
    sol = Solution()
    #print(sol.twoSum([7,2,15,11,30], 22))
    print(sol.twoSum([3,2,4], 6))  # [1,2]
    print(sol.twoSum([3,3], 6))  # [0,1]
