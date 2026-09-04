# Title: Median of Two Sorted Arrays
# Submission ID: 2131017947
# Status: Accepted
# Date: September 4, 2026 at 11:37:31 PM GMT+5:30

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            # Partition nums1
            partition1 = (left + right) // 2

            # Partition nums2 so that left half has half of total elements
            partition2 = (m + n + 1) // 2 - partition1

            # Elements immediately around the partitions
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # Odd total number of elements
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))

                # Even total number of elements
                return (max(maxLeft1, maxLeft2) +
                        min(minRight1, minRight2)) / 2.0

            # nums1 partition is too far right
            elif maxLeft1 > minRight2:
                right = partition1 - 1

            # nums1 partition is too far left
            else:
                left = partition1 + 1