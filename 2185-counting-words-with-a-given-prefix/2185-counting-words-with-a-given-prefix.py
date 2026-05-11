class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        
        # Duyệt qua từng từ (word) trong danh sách words
        for word in words:
            # Hàm .startswith() kiểm tra xem chuỗi có bắt đầu bằng tiền tố truyền vào hay không.
            # Nếu có, nó trả về True, ta tăng biến đếm lên 1.
            if word.startswith(pref):
                count += 1
                
        return count