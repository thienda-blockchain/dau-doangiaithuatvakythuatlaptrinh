class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dem_chu = {}  # Tủ dán nhãn để đếm số lượng ký tự trong cửa sổ
        trai = 0      # Cạnh trái của cửa sổ trượt
        ky_luc_dai_nhat = 0
        
        # Biến lưu giữ "số lượng của chữ cái xuất hiện NHIỀU NHẤT" trong cửa sổ
        max_tan_suat = 0
        
        for phai in range(len(s)):
            chu_hien_tai = s[phai]
            
            # Đưa chữ cái mới vào tủ đếm
            dem_chu[chu_hien_tai] = dem_chu.get(chu_hien_tai, 0) + 1
            
            # Cập nhật kỷ lục: Chữ cái nào đang thống trị cửa sổ này?
            max_tan_suat = max(max_tan_suat, dem_chu[chu_hien_tai])
            
            # Công thức vàng: Số chữ cần thay = (Chiều dài cửa sổ) - (Số chữ xuất hiện nhiều nhất)
            chieu_dai_cua_so = phai - trai + 1
            so_chu_can_thay = chieu_dai_cua_so - max_tan_suat
            
            # Nếu số chữ cần thay vượt quá quyền trợ giúp (k)
            # -> Cửa sổ này bị "lỗi", phải thu hẹp lại từ bên trái
            if so_chu_can_thay > k:
                chu_bi_loai = s[trai]
                dem_chu[chu_bi_loai] -= 1  # Xóa chữ bên trái khỏi tủ đếm
                trai += 1                  # Kéo rèm trái vào 1 bước
                
            # Sau khi điều chỉnh, cửa sổ hiện tại chắc chắn hợp lệ
            # Ta đo lại chiều dài và so sánh với kỷ lục cũ (Giống hệt tư duy bài Chứng khoán!)
            ky_luc_dai_nhat = max(ky_luc_dai_nhat, phai - trai + 1)
            
        return ky_luc_dai_nhat