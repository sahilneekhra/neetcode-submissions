class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-1):
            target = -nums[i]
            seen = set()
            for j in range(i+1, len(nums)):
                diff = target - nums[j]
                if diff in seen:
                    temp_list = [nums[i],diff,nums[j]]
                    if temp_list not in ans:
                        ans.append(temp_list)
                else:
                    seen.add(nums[j])
        return ans