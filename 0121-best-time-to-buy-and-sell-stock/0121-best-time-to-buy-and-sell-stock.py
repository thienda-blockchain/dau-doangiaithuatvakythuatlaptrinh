class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
         # Nếu không có ngày nào để giao dịch
        if not prices:
            return 0
            
        # Khởi tạo giá mua thấp nhất là giá của ngày đầu tiên
        gia_mua_thap_nhat = prices[0]
        loi_nhuan_toi_da = 0
        
        # Duyệt qua giá cổ phiếu của từng ngày
        for gia_hom_nay in prices:
            # 1. Cập nhật "đáy": Nếu thấy giá hôm nay rẻ hơn giá mua thấp nhất trước đó
            if gia_hom_nay < gia_mua_thap_nhat:
                gia_mua_thap_nhat = gia_hom_nay
                
            # 2. Chốt lời: Nếu bán hôm nay thì lãi được bao nhiêu?
            loi_nhuan_hom_nay = gia_hom_nay - gia_mua_thap_nhat
            
            # Cập nhật kỷ lục nếu lãi hôm nay cao hơn kỷ lục cũ
            if loi_nhuan_hom_nay > loi_nhuan_toi_da:
                loi_nhuan_toi_da = loi_nhuan_hom_nay
                
        return loi_nhuan_toi_da