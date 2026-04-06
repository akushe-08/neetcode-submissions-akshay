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