class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the strings have the same length
        if len(s) != len(t):
            return False
        # After sorting, if they exactly the same
        return (sorted(s) == sorted(t))