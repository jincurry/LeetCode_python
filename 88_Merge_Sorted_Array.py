# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold
# additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        final, i, j = m+n-1, m-1, n-1
        while i >= 0 and j >= 0:
            if nums1[i] <nums2[j]:
                nums1[final] = nums2[j]
                final = final - 1
                j = j -1
            else:
                nums1[final] = nums1[i]
                final = final - 1
                i = i - 1
        while j >= 0:
            nums1[j] = nums2[j]
            j = j - 1
        return nums1


if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([1,3,5,7,9,0,0,0,0],5,[2,4,6,8],4))
