class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_set = {"a", "e", "i", "o", "u"}

        def vowelCount(v: str) -> int:
            count = 0
            for i in v:
                if i in vowel_set:
                    count += 1

            return count

        curr_count = vowelCount(s[:k])

        max_count = curr_count

        for i in range(k, len(s)):

            if s[i - k] in vowel_set:
                curr_count -= 1

            if s[i] in vowel_set:
                curr_count += 1

            max_count = max(max_count, curr_count)

        return max_count


def test_solution(s, k, expected):
    solution = Solution()
    result = solution.maxVowels(s, k)
    print(f"Input: s = '{s}', k = {k}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Normal case with multiple vowels
    test_solution("abciiidef", 3, 3)

    # Test Case 2: No vowels in the string
    test_solution("bcdfghjklmnpqrstvwxyz", 5, 0)

    # Test Case 3: All vowels
    test_solution("aeiou", 5, 5)

    # Test Case 4: Mixed characters
    test_solution("leetcode", 3, 3)

    # Test Case 5: Length of k equals string length
    test_solution("abcde", 5, 2)

    # Test Case 6: Length of k is 1
    test_solution("hello", 1, 1)

    # Test Case 7: Single vowel at the end
    test_solution("xyzxoz", 3, 1)

    # Test Case 8: Large string with repeated vowels
    test_solution("aaabbbcccddddeeeeffff", 6, 4)

    # Test Case 9: String with alternating vowels and consonants
    test_solution("aebecid", 4, 3)
