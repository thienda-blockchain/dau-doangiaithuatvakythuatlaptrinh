class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # Trường hợp ngoại lệ: Nếu chỉ có đúng 1 người trong thị trấn 
        # và không có ai tin ai (trust rỗng), người đó nghiễm nhiên là Thẩm phán.
        if n == 1 and not trust:
            return 1
            
        # Tạo một mảng "Sổ điểm" để ghi nhận điểm niềm tin của từng người.
        # Kích thước (n + 1) để chỉ số mảng khớp luôn với tên người (từ 1 đến n).
        # Bỏ qua chỉ số 0.
        diem_niem_tin = [0] * (n + 1)
        
        # Duyệt qua từng mối quan hệ [a, b] (người a tin người b)
        for a, b in trust:
            # Người 'a' đem lòng tin người khác -> Bị trừ 1 điểm
            # (Chắc chắn 'a' không thể là Thẩm phán vì Thẩm phán không tin ai)
            diem_niem_tin[a] -= 1
            
            # Người 'b' được nhận niềm tin -> Được cộng 1 điểm
            diem_niem_tin[b] += 1
            
        # Cuộc bầu chọn: Tìm xem ai là người đạt điểm tuyệt đối?
        # Thẩm phán phải được TẤT CẢ những người còn lại tin tưởng (n - 1 người)
        # và không bị trừ điểm nào. Vậy điểm của Thẩm phán phải ĐÚNG BẰNG n - 1.
        for i in range(1, n + 1):
            if diem_niem_tin[i] == n - 1:
                return i
                
        # Nếu không có ai đạt đủ số điểm n - 1, thị trấn không có Thẩm phán
        return -1