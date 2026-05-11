class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
         # BƯỚC 1: Lọc chuỗi (Chỉ giữ lại chữ và số, đồng thời viết thường)
        # Lệnh duyệt qua từng ký tự 'c' trong chuỗi 's'
        # Nếu 'c' là chữ hoặc số (c.isalnum()), ta sẽ đổi nó thành chữ thường (c.lower())
        chuoi_sach = [c.lower() for c in s if c.isalnum()]
        
        # BƯỚC 2: So sánh chuỗi với chính nó khi bị đảo ngược
        # Cú pháp [::-1] là một "phép thuật" của Python giúp lật ngược mảng/chuỗi ngay lập tức
        return chuoi_sach == chuoi_sach[::-1]