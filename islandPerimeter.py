class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # Convert grid to tuple-keyed dictionary

        # Create perimeter placeholder
        # For location in dictionary
            # If item value is 1
                # Give it a starting value of 4
                # Look around it in non-zero directions
                # If surrounding value is a 1, subtract from 4
