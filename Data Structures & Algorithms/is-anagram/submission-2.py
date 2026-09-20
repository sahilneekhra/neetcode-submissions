class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        def map_the_string(s: str) -> dict:
            d = {}
            for i in s:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            return d
        map_s = map_the_string(s)
        map_t = map_the_string(t)
        if map_s == map_t:
            return True
        else:
            return False





        