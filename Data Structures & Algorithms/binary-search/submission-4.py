class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l = 0
        r = length
        while l < r:
            add = r+l
            if nums[add//2] > target:
                r = add//2
            elif nums[add//2]< target:
                l = add//2 +1
            else:
                return add // 2
        return -1
                