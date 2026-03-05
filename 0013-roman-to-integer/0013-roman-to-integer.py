class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        gia_tri = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        tong = 0

        for i in range(len(s)):
            so_hien_tai = gia_tri[s[i]]

            if i + 1 < len(s) and so_hien_tai < gia_tri[s[i+1]]:
                tong -= so_hien_tai
            else:
                tong += so_hien_tai
            
        return tong
