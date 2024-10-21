class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}

        left_ptr = 0
        maxf = 0
        for right_ptr in range(len(s)):
            count_map[s[right_ptr]] = 1 + count_map.get(s[right_ptr], 0)
            maxf = max(maxf, count_map[s[right_ptr]])

            if (right_ptr - left_ptr + 1) - maxf > k:
                count_map[s[left_ptr]] -= 1
                left_ptr += 1

        return (right_ptr - left_ptr) + 1
