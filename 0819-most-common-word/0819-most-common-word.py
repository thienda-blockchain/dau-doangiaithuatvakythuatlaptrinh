class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
         # Chuyển về chữ thường
        paragraph = paragraph.lower()
        
        # Thay thế các dấu câu bằng khoảng trắng
        # Các ký tự cần loại bỏ: ! ? ' , ; .
        lam_sach = ""
        for ky_tu in paragraph:
            if ky_tu.isalpha(): # Nếu là chữ cái thì giữ lại
                lam_sach += ky_tu
            else: # Nếu là dấu câu hoặc khoảng trắng thì biến hết thành dấu cách
                lam_sach += " "
        
        #Tách thành danh sách các từ
        cac_tu = lam_sach.split()
        
        #Đưa danh sách cấm vào Set để tra cứu nhanh
        tui_cam = set(banned)
        
        # Đếm số lần xuất hiện bằng Dictionary
        dem_tu = {}
        for tu in cac_tu:
            # Chỉ đếm nếu từ đó KHÔNG nằm trong danh sách cấm
            if tu not in tui_cam:
                dem_tu[tu] = dem_tu.get(tu, 0) + 1
        
        # Bước 5: Tìm từ có số lần xuất hiện cao nhất
        tu_max = ""
        so_lan_max = 0
        
        for tu in dem_tu:
            if dem_tu[tu] > so_lan_max:
                so_lan_max = dem_tu[tu]
                tu_max = tu
                
        return tu_max