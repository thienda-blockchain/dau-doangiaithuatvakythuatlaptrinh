class MinStack(object):

    def __init__(self):
        # Khởi tạo một mảng lưu trữ theo từng cặp (tuple)
        # Mỗi phần tử trong stack sẽ có dạng: (giá trị_thực, giá trị_nhỏ_nhất_hiện_tại)
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            # Nếu stack rỗng, giá trị nhỏ nhất cũng chính là val
            self.stack.append((val, val))
        else:
            # Lấy giá trị nhỏ nhất ở "tầng" ngay dưới nó (tại đỉnh stack cũ)
            min_cu = self.stack[-1][1]
            
            # Tính toán min mới: so sánh val với min cũ
            min_moi = min(val, min_cu)
            
            # Đóng gói val và min mới thành một cặp, rồi đẩy vào stack
            self.stack.append((val, min_moi))
        

    def pop(self):
        """
        :rtype: None
        """
        # pop() trong Python tự động vứt bỏ phần tử trên cùng
        if self.stack:
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        # Trả về giá_trị_thực (phần tử số 0 của tuple trên đỉnh)
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        # Trả về giá_trị_nhỏ_nhất_hiện_tại (phần tử số 1 của tuple trên đỉnh)
        if self.stack:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()