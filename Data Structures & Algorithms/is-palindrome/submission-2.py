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
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue
            if s[p1].isalnum() and s[p2].isalnum():
                if s[p1].lower() == s[p2].lower():
                    p1 += 1
                    p2 -= 1
                else:
                    return False
        return True

                
                
            

    

        return True
        