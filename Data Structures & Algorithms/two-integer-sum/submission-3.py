class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen maps: number -> index where we first/last saw it earlier
        # Main idea:
        # for current num, check whether target - num was already seen
        seen = {}

        for index, num in enumerate(nums):
            # Needed value to complete the target sum
            complement = target - num

            # If complement was seen earlier, we found the pair
            # Important:
            # seen[complement] is guaranteed to be a smaller index
            # because we scan left to right
            if complement in seen:
                return [seen[complement], index]

            # Store current number after checking
            # This avoids using the same element twice
            seen[num] = index