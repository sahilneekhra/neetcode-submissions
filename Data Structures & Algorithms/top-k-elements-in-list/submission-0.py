import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] +=1
            else:
                freq_dict[i] = 1
        
        heap = []

        for i in freq_dict:
            heapq.heappush(heap,(-freq_dict[i], i))
        
        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

        
        