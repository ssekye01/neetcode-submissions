class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j = 0, k
        curr_max = max(nums[i:j])
        freq = Counter(nums[i:j])
        result = [curr_max]

        for count in range(len(nums) - k):
            freq[nums[i]] -= 1
            freq[nums[j]] += 1

            if nums[j] > curr_max:
                curr_max = nums[j]
            elif nums[i] == curr_max and freq[nums[i]] == 0:
                curr_max = max(nums[i + 1:j + 1])

            i += 1
            j += 1

            result.append(curr_max)

        return result