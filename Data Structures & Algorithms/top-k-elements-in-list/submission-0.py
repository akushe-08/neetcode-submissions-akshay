class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for item in nums:
            count_dict[item] = count_dict.get(item, 0) + 1

        # Sort items by frequency in descending order and take the top k
        sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]