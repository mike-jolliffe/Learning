class Solution:
    def moveZeroes(self, nums):
        """Moves all zeroes in array to end, modifying in-place
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
        print(nums)


if __name__ == '__main__':
    sol = Solution()
    sol.moveZeroes([0,1,0,3,5,0,12,0])
