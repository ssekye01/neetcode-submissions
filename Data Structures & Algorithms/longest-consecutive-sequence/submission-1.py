class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        n = len(nums)
        for track in range(n):
            if nums[track] - 1 not in num_set:
                streak = 1
                curr = nums[track]
                while curr + 1 in num_set:
                    streak += 1
                    curr += 1
                longest = max(streak, longest)
        return longest