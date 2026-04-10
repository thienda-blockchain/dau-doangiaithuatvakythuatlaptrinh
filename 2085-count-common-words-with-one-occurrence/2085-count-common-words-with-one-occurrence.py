class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        dem1 = {}
        dem2 = {}
        
        for word in words1:
            dem1[word] = dem1.get(word, 0) + 1
            
        for word in words2:
            dem2[word] = dem2.get(word, 0) + 1
            
        # Bước 2: Duyệt qua các từ trong dem1 theo đúng ý tưởng của bạn
        ket_qua = 0
        for tu, so_luong in dem1.items():
            # Điều kiện 1: Từ đó xuất hiện ĐÚNG 1 LẦN ở mảng 1
            if so_luong == 1:
                # Điều kiện 2: Từ đó cũng xuất hiện ĐÚNG 1 LẦN ở mảng 2
                if dem2.get(tu, 0) == 1:
                    ket_qua += 1
                    
        return ket_qua