class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        
        dem = {}
        # Duyệt từ quả bóng lowLimit đến highLimit
        for i in range(lowLimit, highLimit + 1):
             # Tính tổng các chữ số của quả bóng i
            tong_chu_so = 0
            while i > 0:
                tong_chu_so += i % 10  # Lấy chữ số cuối
                i //= 10              # Bỏ chữ số cuối
            
            # Bỏ quả bóng vào hộp (tăng số lượng trong Dictionary)
            # Nếu hộp chưa có bóng, mặc định là 0 rồi cộng thêm 1
            dem[tong_chu_so] = dem.get(tong_chu_so, 0) + 1
        
        # dem.values() trả về danh sách các số lượng quả bóng
        return max(dem.values())