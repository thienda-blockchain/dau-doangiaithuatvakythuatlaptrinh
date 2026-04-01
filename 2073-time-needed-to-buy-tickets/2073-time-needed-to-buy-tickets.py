class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        tong_thoi_gian = 0
        so_ve_k_muon = tickets[k]
        
        for i in range(len(tickets)):
            # Nhóm 1: Những người đứng trước K và chính bạn K
            if i <= k:
                # Họ mua tối đa bằng số vé của K
                tong_thoi_gian += min(tickets[i], so_ve_k_muon)
            
            # Nhóm 2: Những người đứng sau K
            else:
                # Họ chỉ kịp mua tối đa (số vé của K - 1)
                # Vì K mua xong là đồng hồ dừng lại ngay lập tức
                tong_thoi_gian += min(tickets[i], so_ve_k_muon - 1)
                
        return tong_thoi_gian