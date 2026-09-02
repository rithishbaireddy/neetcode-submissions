class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 0:
            return 0

        count = 1
        max_count = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff == 1:
                count += 1

            elif diff == 0:
                continue

            else:
                count = 1

            max_count = max(max_count, count)

        return max_count      



        
            