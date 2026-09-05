class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                # Remove leftmost character 
                seen.remove(s[left])
                left += 1
            # Add current character
            seen.add(s[right])
            # Record size of the current window
            max_length = max(max_length, right - left + 1)
        return max_length

