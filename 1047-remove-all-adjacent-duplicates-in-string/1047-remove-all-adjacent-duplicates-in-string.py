class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
         # Khởi tạo một Stack (Ngăn xếp) rỗng
        # Trong Python, ta dùng list (danh sách) để làm Stack
        stack = []
        
        # Duyệt qua từng chữ cái trong chuỗi
        for chu in s:
            
            # Kiểm tra 2 điều kiện:
            # 1. Stack đang có đồ vật bên trong (stack không rỗng)
            # 2. Chữ cái ta đang cầm trên tay GIỐNG HỆT chữ cái nằm trên cùng của Stack (stack[-1])
            if stack and stack[-1] == chu:
                # BÙM! Hai chữ cái giống nhau triệt tiêu lẫn nhau.
                # Ta vứt chữ cái trên cùng của Stack đi, và cũng không bỏ chữ trên tay vào nữa.
                stack.pop()
                
            else:
                # Nếu không giống nhau (hoặc Stack đang trống), 
                # ta thả chữ cái đang cầm vào Stack.
                stack.append(chu)
                
        # Cuối cùng, ghép các chữ cái còn sống sót trong Stack lại thành chuỗi
        return "".join(stack)