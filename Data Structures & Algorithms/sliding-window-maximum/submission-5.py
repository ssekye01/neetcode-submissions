class Solution:
    import heapq
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            start = i - k + 1
            while heap[0][1] < start:
                heapq.heappop(heap)
            if i >= k - 1:
                result.append(-heap[0][0])
        return result
