class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        temp_set = set()
        ans = 0

        while right < len(s):
            while s[right] in temp_set:
                temp_set.remove(s[left])
                left += 1

            temp_set.add(s[right])
            ans = max(ans, len(temp_set))
            right += 1

        return ans