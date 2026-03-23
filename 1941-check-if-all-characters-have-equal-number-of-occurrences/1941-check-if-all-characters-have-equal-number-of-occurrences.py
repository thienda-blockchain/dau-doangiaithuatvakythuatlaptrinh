class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = {}
        for chu_cai in s:
            check[chu_cai] = check.get(chu_cai, 0) + 1

        # Lấy danh sách tất cả các giá trị (tần suất) trong túi check
        tan_suat_cac_chu = check.values()
        
        # Lấy giá trị đầu tiên làm mốc so sánh
        # Chuyển về list để lấy được phần tử ở vị trí số 0
        danh_sach_so_lan = list(tan_suat_cac_chu)
        so_lan_chuan = danh_sach_so_lan[0]
        
        # So sánh tất cả các số còn lại với số chuẩn
        for so_lan in danh_sach_so_lan:
            if so_lan != so_lan_chuan:
                return False
                
        return True