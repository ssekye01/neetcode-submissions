class Solution:
    import heapq
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        frequency = Counter(nums)
        for num, freq in frequency.items():
            heapq.heappush(heap, [freq, num])
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]

