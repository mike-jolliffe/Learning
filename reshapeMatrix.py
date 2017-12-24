class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        # Get current matrix dims
        r_curr = len(nums)
        c_curr = len(nums[0])

        # If current dims can't be reshaped into desired
        if r_curr * c_curr != r * c:
            # Return orig matrix
            return nums
        else:
            # Flatten to 1-D array
            flat = []
            for row in nums:
                for val in row:
                    flat.append(val)
            print("Flattened array: {}".format(flat))
            # Iterate through 1D, splitting into rows
            col_counter = 0
            row_counter = 0
            reshaped = []
            row = []
            for i in range(len(flat)):
                # Complete a single row by matching up to col length
                if col_counter < c:
                    row.append(flat[i])
                    col_counter += 1
                elif row_counter < r:
                    reshaped.append(row)
                    row = []
                    col_counter = 0
                    row.append(flat[i])
                    col_counter += 1
                    row_counter += 1
            reshaped.append(row)
            return reshaped

if __name__ == '__main__':
    sol = Solution()
    print(sol.matrixReshape([[1,2],[3,4]], 1, 4))
    print(sol.matrixReshape([[1,2],[3,4]], 1, 3))
    print(sol.matrixReshape([[1,2,3,4]], 2, 2))
