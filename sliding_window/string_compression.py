from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1

        return ans


if __name__ == "__main__":
    chars = ["a", "a", "a", "a", "b", "b", "c", "c", "c"]

    s = Solution()
    print(s.compress(chars))
