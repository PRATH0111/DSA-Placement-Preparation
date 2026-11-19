class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        k = n - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[k] = left_square
                left += 1
            else:
                result[k] = right_square
                right -= 1

            k -= 1

        return result