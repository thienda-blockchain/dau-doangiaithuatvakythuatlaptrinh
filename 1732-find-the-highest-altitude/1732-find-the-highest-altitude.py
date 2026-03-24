class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # mảng "lưu kết quả
        altitudes = [0]
        
        # Duyệt qua từng mức tăng/giảm trong mảng gain
        for i in range(len(gain)):
            # Độ cao mới = Độ cao hiện tại + mức thay đổi tiếp theo
            do_cao_moi = altitudes[-1] + gain[i]
            # Lưu kết quả mới vào mảng altitudes
            altitudes.append(do_cao_moi)
            
        # So sánh và tìm giá trị lớn nhất (max) trong mảng kết quả
        return max(altitudes)