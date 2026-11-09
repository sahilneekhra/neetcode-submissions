class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos = list(zip(position,speed))
        pos_sort = sorted(pos,reverse=True)
        prev = 0
        res = 0
        for p,s in pos_sort:
            pToTarget = (target - p) / s
            if prev < pToTarget:
                res+=1
                prev = pToTarget
            else:
                continue
        return res