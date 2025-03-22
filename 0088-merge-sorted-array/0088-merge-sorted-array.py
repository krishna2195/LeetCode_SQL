class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m-1  # Last element in nums1
        p2 = n-1  # Last element in nums2
        p= n+m-1  # last element in merged array
        
        while p1>=0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -=1
            
            else:
                nums1[p]= nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >=0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1