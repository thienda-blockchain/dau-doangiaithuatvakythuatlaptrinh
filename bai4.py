class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        mang_tong = nums1 + nums2

        mang_tong.sort()

        n = len(mang_tong)

        if n % 2 != 0:
            return float(mang_tong[n//2])
        else:
            so_ben_trai = mang_tong[(n//2)-1]
            so_ben_phai = mang_tong[n//2]
            return ((float(so_ben_trai)+float(so_ben_phai))/2)


        