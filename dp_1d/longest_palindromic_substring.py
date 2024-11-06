class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            odd = self.expand_from_center(s, i, i)
            even = self.expand_from_center(s, i, i + 1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end+1]

        return

    def expand_from_center(self, s: str, l: int, r: int):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1


def test_solution(s, expected):
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(f"Input: s = '{s}'")
    print(f"Expected: '{expected}', Got: '{result}'")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Odd-length palindrome
    test_solution("babad", "bab")  # "aba" is also valid

    # Test Case 2: Even-length palindrome
    test_solution("cbbd", "bb")

    # Test Case 3: Single character
    test_solution("a", "a")

    # Test Case 4: Entire string is a palindrome
    test_solution("racecar", "racecar")

    # Test Case 5: All characters the same
    test_solution("aaaa", "aaaa")

    # Test Case 6: No palindrome longer than one character
    test_solution("abc", "a")  # "b" or "c" is also valid

    # Test Case 7: Mixed case with multiple palindromic options
    test_solution("abacdfgdcaba", "aba")

    # Test Case 8: Empty string
    test_solution("", "")

    # Test Case 9: Long palindrome in the middle
    test_solution("abaxyzzyxf", "xyzzyx")

    # Test Case 10: Complex case with multiple palindromes
    test_solution("forgeeksskeegfor", "geeksskeeg")
