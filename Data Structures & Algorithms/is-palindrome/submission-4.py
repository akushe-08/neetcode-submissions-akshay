# =========================================================
# Valid Palindrome
# A palindrome reads the same forwards and backwards,
# considering only alphanumeric chars and ignoring case.
# =========================================================


# ---------------------------------------------------------
# Approach 1: Brute Force (build cleaned string, compare with reverse)
# Time:  O(n)  -- one pass to clean, one pass to reverse, one pass to compare
# Space: O(n)  -- we build new strings (s_clean, s_rev_clean)
# ---------------------------------------------------------
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # Keep only alphanumeric chars, lowercase everything
#         s_clean = "".join(ch for ch in s if ch.isalnum()).lower()
#
#         # Reverse the cleaned string
#         s_rev_clean = s_clean[::-1]
#
#         # A palindrome equals its reverse
#         return s_clean == s_rev_clean


# ---------------------------------------------------------
# Approach 2: Two Pointers (in-place, optimal)
# Time:  O(n)  -- each char is visited at most once
# Space: O(1)  -- only two integer pointers, no extra string built
# ---------------------------------------------------------
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers: one at the start, one at the end
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric chars on the LEFT
            if not s[left].isalnum():
                left += 1
                continue

            # Skip non-alphanumeric chars on the RIGHT
            if not s[right].isalnum():
                right -= 1
                continue

            # Both chars are alphanumeric -> compare (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            # Matched -> move both pointers inward
            left += 1
            right -= 1

        # All comparisons passed (or pointers met in the middle)
        return True