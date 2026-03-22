class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)
        if len(s) <= 3:
            return s
            
        ket_qua = ""
        bien_dem = 0
        
        # Chạy vòng lặp từ cuối chuỗi lên đầu chuỗi
        for i in range(len(s) - 1, -1, -1):
            
            # Nhặt chữ số hiện tại bỏ vào phía trước chuỗi kết quả
            ket_qua = s[i] + ket_qua
            bien_dem += 1
            
            # Nếu đã đếm đủ 3 chữ số VÀ phía trước vẫn còn chữ số nữa
            # (i != 0 nghĩa là chưa phải chữ số đầu tiên của n)
            if bien_dem == 3 and i != 0:
                # Thêm dấu chấm vào phía trước
                ket_qua = "." + ket_qua
                # Reset bộ đếm về 0 để đếm 3 chữ số tiếp theo
                bien_dem = 0
        return ket_qua