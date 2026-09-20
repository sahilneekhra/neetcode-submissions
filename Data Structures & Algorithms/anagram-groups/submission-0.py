class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j.lower()) - ord('a')] += 1
            d[tuple(count)].append(i)
        return list(d.values())
        