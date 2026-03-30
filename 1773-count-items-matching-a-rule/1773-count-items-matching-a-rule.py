class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        check_index = 0
        if ruleKey == "color":
            check_index = 1
        elif ruleKey == "name":
            check_index = 2
            
        # Chuẩn bị máy đếm
        count = 0
        
        # Duyệt qua từng món đồ trong kho
        for item in items:
            # Kiểm tra xem thông tin tại vị trí check_index 
            if item[check_index] == ruleValue:
                count += 1
                
        return count