class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = list(set(nums))
        l = len(s)
        if l == 1:
            return 1
        s.sort()
        res = 0
        temp = 1
        print(s)
        for i in range(len(s)-1):
            if s[i+1] == s[i] + 1:
                temp += 1
            else:
                temp = 1
            res = max(res,temp)
        return res