class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            elif nums[i] not in seen:
                seen[nums[i]] = i
            else:
                continue
        
        