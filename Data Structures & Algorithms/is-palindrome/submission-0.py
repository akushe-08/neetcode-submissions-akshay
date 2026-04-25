# Brute Force

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s_clean = "".join([ch for ch in s if ch.isalnum()])
#         s_rev_clean = "".join([ch for ch in s[::-1] if ch.isalnum()])
#         if s_clean.lower() == s_rev_clean.lower():
#             return True
#         return False
        
# Two Pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join([ch for ch in s if ch.isalnum()])
        s_clean = s_clean.lower()
        p1 = 0
        p2 = len(s_clean) - 1

        while p1 < p2:
            if s_clean[p1] == s_clean[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False

        return True
        