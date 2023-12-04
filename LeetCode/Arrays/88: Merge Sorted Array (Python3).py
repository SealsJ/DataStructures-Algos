class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Achieve the last index of nums1 to go backwards
        last = m + n - 1

        #merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        #fill nums1 with remaining elements in nums 2 ***EDGE CASE***
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1


        #TC: O(n) / SC: O(1)
