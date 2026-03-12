class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        ket_qua = []
        for chu in s:
            # Lấy "con số" (mã ASCII) của ký tự đó bằng hàm ord()
            ma_ascii = ord(chu)
            if 65 <= ma_ascii <= 90:
                ma_chu_thuong = ma_ascii + 32
                # Đổi con số mới này ngược lại thành chữ bằng hàm chr()
                ket_qua.append(chr(ma_chu_thuong))
            else:
                ket_qua.append(chu)
        return "".join(ket_qua)