class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have equal length
        if len(s) != len(t):
            return False

        # Frequency delta across 26 lowercase letters;
        # increments for s, decrements for t — anagram iff all zeros
        alphas = [0] * 26
        for i in range(len(s)):
            alphas[ord(s[i]) - ord('a')] += 1
            alphas[ord(t[i]) - ord('a')] -= 1

        return not any(alphas)


"""
Doubts and explanations:

1. Can alphas contain negative numbers?
Yes. Each entry in alphas stores:
count_in_s - count_in_t

So if a character appears more times in t than in s, that entry becomes negative.
Example:
s = "ab", t = "bb"
For 'b', the final balance is -1.

2. Then why does return not any(alphas) still work?
Because any(alphas) checks whether at least one element is truthy.
In Python, 0 is falsy, and any non-zero number is truthy, including negative numbers.
So:
any(alphas) == True  means at least one count is not zero
any(alphas) == False means all counts are zero

3. What if alphas contains only negative numbers and zeros?
It still works correctly.
Negative numbers are also non-zero, so they are truthy.
That means any(alphas) will return True, and not any(alphas) will return False.

4. Why is that correct for an anagram check?
For two strings to be anagrams, every character count must cancel out exactly.
That means every entry in alphas must be 0.
So:
return not any(alphas)
is equivalent to:
return all(x == 0 for x in alphas)

5. Final intuition
alphas is a balance sheet:
0  -> counts match
+  -> extra occurrences in s
-  -> extra occurrences in t

An anagram is valid only when every balance is zero.
"""