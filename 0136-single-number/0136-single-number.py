class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Khởi tạo kết quả ban đầu là 0
        ket_qua = 0
        
        # Duyệt qua từng con số trong mảng
        for so in nums:
            # Dùng phép toán Bitwise XOR (^=)
            # Phép toán này sẽ tự động triệt tiêu các cặp số giống nhau thành 0
            # và giữ lại con số duy nhất không có cặp.
            ket_qua ^= so
            
        return ket_qua

        # ---------------------------------------------------------
        # CÁCH 2: DÙNG TOÁN HỌC & SET (Dễ hiểu nhưng tốn O(N) bộ nhớ)
        # ---------------------------------------------------------
        # Tổng của Set (đã loại bỏ trùng) nhân 2, trừ đi Tổng của mảng gốc
        # Ví dụ: nums = [4, 1, 2, 1, 2]
        # Set = {1, 2, 4} -> Tổng = 7. Nhân 2 = 14
        # Tổng mảng gốc = 4 + 1 + 2 + 1 + 2 = 10
        # Kẻ độc thân = 14 - 10 = 4
        # 
        # return 2 * sum(set(nums)) - sum(nums)