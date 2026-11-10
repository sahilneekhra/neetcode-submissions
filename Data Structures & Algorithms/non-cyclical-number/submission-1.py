class Solution:
    def isHappy(self, n: int) -> bool:
        def sq_sum(num):
            if num//10 == 0:
                return ((num%10)**2)
            else:
                return ((num%10)**2) + sq_sum(num//10)
        s = set()
        while n not in s:
            temp = sq_sum(n)
            print(f"temp ={temp}")
            if temp == 1:
                return True
            else:
                s.add(n)
                n = temp
        print(s)
        return False
