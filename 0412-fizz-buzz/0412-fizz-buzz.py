class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ket_qua = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ket_qua.append("FizzBuzz")
            elif i % 5 == 0:
                ket_qua.append("Buzz")
            elif i % 3 == 0:
                ket_qua.append("Fizz")
            else:
                ket_qua.append(str(i))
            
        return ket_qua 
                