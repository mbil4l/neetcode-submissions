class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        p1, p2 = 0, 0
        curr = []

        while p1 < m and p2 < n:

            if nums1[p1] <= nums2[p2]:
                curr.append(nums1[p1])
                p1 += 1 
            else:
                curr.append(nums2[p2])
                p2 += 1

        if p1 == m:
            curr.extend(nums2[p2:]) 
        else:
            curr.extend(nums1[p1:])

        if (m + n) % 2 != 0:
            return float(curr[(m + n) // 2])
        else:
            return (curr[(m+n) // 2] + curr[(m+n) // 2 - 1]) / 2.0