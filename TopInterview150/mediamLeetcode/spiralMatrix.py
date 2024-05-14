class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        results = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
        # Traverse from left to right along the top row
            for i in range(left, right + 1):
              results.append(matrix[top][i])
            top += 1

        # Traverse downwards along the right column
            for i in range(top, bottom + 1):
             results.append(matrix[i][right])
            right -= 1

            if top <= bottom:
            # Traverse from right to left along the bottom row
               for i in range(right, left - 1, -1):
                results.append(matrix[bottom][i])
            bottom -= 1

            if left <= right:
            # Traverse upwards along the left column
              for i in range(bottom, top - 1, -1):
                results.append(matrix[i][left])
            left += 1

        return results