class Solution:
    def intersect(self, nums1, nums2):
        count = {}

        for num in nums1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        result = []

        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result