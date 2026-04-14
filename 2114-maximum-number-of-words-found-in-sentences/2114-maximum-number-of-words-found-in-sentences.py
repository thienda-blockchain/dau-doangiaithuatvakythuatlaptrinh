class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        #Tạo một biến để lưu số lượng từ lớn nhất
        max_tu = 0
        
        # Duyệt qua từng câu trong danh sách 'sentences'
        # Mỗi 's' ở đây là một câu hoàn chỉnh
        for s in sentences:
            
            # Dùng split() để tách câu thành danh sách các từ
            # Mặc định split() sẽ tách dựa trên khoảng trắng
            danh_sach_tu = s.split()
            
            #Dùng len() để đếm xem có bao nhiêu từ trong danh sách đó
            so_luong = len(danh_sach_tu)
            
            if so_luong > max_tu:
                max_tu = so_luong
                
        # Trả về kết quả cuối cùng sau khi đã kiểm tra hết tất cả các câu
        return max_tu