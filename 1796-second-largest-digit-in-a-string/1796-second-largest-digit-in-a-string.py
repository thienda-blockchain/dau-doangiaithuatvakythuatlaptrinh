class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        chu_so_duy_nhat = set()
        
        for ky_tu in s:
            # Kiểm tra xem ký tự đó có phải là số không
            if ky_tu.isdigit():
                # Chuyển ký tự thành số nguyên và bỏ vào tập hợp
                chu_so_duy_nhat.add(int(ky_tu))
        

        # Chuyển tập hợp thành danh sách và sắp xếp tăng dần
        danh_sach_so = sorted(list(chu_so_duy_nhat))
        
        # Nếu danh sách chỉ được một số, nghĩa là không có số lớn thứ hai
        if len(danh_sach_so) < 2:
            return -1
        
        # Trả về số lớn thứ hai (số đứng ở vị trí thứ 2 từ cuối lên)
        return danh_sach_so[-2]