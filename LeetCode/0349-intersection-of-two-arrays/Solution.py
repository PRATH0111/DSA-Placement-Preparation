class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        result = []

        for num in nums2:
            if num in set1 and num not in result:
                result.append(num)

        return result