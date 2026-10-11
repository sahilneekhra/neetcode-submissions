class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0] * n
        mono_stack = []
        for i in range(len(temperatures)):
            if not mono_stack or mono_stack[-1][0] > temperatures[i]:
                mono_stack.append((temperatures[i],i))
            else:
                while mono_stack and mono_stack[-1][0] < temperatures[i]:
                    idx = mono_stack[-1][1]
                    res[idx] = i - idx
                    mono_stack.pop()
                mono_stack.append((temperatures[i],i))
        return res

