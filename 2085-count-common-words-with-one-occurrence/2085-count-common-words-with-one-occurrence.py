class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        def lay_tu_duy_nhat(danh_sach):
            da_thay = set()
            bi_lap = set()
            for tu in danh_sach:
                if tu in da_thay:
                    bi_lap.add(tu)
                da_thay.add(tu)
            # Từ duy nhất = Tất cả các từ đã thấy - Các từ bị lặp
            return da_thay - bi_lap

        # Bước 1: Tìm tập hợp các từ xuất hiện đúng 1 lần trong mảng 1
        set1 = lay_tu_duy_nhat(words1)
        
        # Bước 2: Tìm tập hợp các từ xuất hiện đúng 1 lần trong mảng 2
        set2 = lay_tu_duy_nhat(words2)
        
        # Bước 3: Kết quả là số lượng phần tử CHUNG của 2 tập hợp này
        # Phép toán & (intersection) tìm các phần tử có ở cả 2 tập hợp
        tu_chung_duy_nhat = set1 & set2
        
        return len(tu_chung_duy_nhat)