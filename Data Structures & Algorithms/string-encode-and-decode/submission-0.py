class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s = s + str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        l=[]
        count = 0 
        while count<len(s):
            num = ""

            while count<len(s) and s[count] != "#":
                num = num + s[count]
                count+=1
            count+=1

            it = int(num)
            word = ""
            for i in range(it):
                word = word + s[count+i]

            l.append(word)
            count+=it
            
        return l
