class Solution:
    def countSegments(self, s: str) -> int:
        l = 0
        count = 0

        while l < len(s):

            while l < len(s) and s[l] == " ":
                l += 1

            if l >= len(s):
                break

            count += 1

            while l < len(s) and s[l] != " ":
                l += 1

        return count


def test_solution(s, expected):
    solution = Solution()
    result = solution.countSegments(s)
    print(f"Input: s = '{s}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Normal case with multiple segments
    test_solution("Hello, my name is John", 5)

    # Test Case 2: String with extra spaces
    test_solution("  Hello   world  ", 2)

    # Test Case 3: Empty string
    test_solution("", 0)

    # Test Case 4: String with only spaces
    test_solution("     ", 0)

    # Test Case 5: Single word
    test_solution("Hello", 1)

    # Test Case 6: Multiple spaces between words
    test_solution("One  Two   Three", 3)

    # Test Case 7: Special characters included
    test_solution("A! B@ C# D$", 4)

    # Test Case 8: Digits and letters
    test_solution("123 456 789", 3)

    # Test Case 9: String with newline characters
    test_solution("Line1 Line2 Line3", 3)

    # Test Case 10: Mixed content
    test_solution("  Mix   of words  and numbers 12345 ", 5)
