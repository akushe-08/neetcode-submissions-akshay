
# Naive solution


# from collections import defaultdict
# from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # Key idea of naive solution:
#         # if two words are anagrams, their sorted characters will be the same
#         # Example:
#         # "act" -> ('a', 'c', 't')
#         # "cat" -> ('a', 'c', 't')
#         groups = defaultdict(list)

#         for word in strs:
#             # Sort the characters of the word
#             # Use tuple because it can be used as a dictionary key
#             sorted_word = tuple(sorted(word))

#             # Put this word into its anagram group
#             groups[sorted_word].append(word)

#         # We only need the grouped lists as the final answer
#         return list(groups.values())


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash map:
        # key   -> 26-length frequency signature of a word
        # value -> list of words with that same signature
        # defaultdict(list) lets us append without checking if key exists first
        res = defaultdict(list)

        for s in strs:
            # Count frequency of each lowercase letter in the current word
            # count[0]  -> frequency of 'a'
            # count[1]  -> frequency of 'b'
            # ...
            # count[25] -> frequency of 'z'
            count = [0] * 26

            for c in s:
                # Convert character to 0-based alphabet index
                # ord('a') - ord('a') = 0
                # ord('b') - ord('a') = 1
                # ...
                count[ord(c) - ord('a')] += 1

            # Use tuple(count) as dictionary key because lists are not hashable
            # All anagrams produce the same 26-count signature
            res[tuple(count)].append(s)

        # Return only the grouped anagram lists
        return list(res.values())







