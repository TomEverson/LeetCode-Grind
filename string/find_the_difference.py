class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        hashmap = {}

        if not s:
            return t

        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1

        for l in t:
            if l not in hashmap or hashmap[l] == 0:
                return l
            hashmap[l] = hashmap[l] - 1

        return


def test_solution(s, t, expected):
    solution = Solution()
    result = solution.findTheDifference(s, t)
    print(f"Input: s = '{s}', t = '{t}'")
    print(f"Expected: '{expected}', Got: '{result}'")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Simple case with one extra character
    test_solution("abcd", "abcde", "e")

    # Test Case 2: Extra character is the first character
    test_solution("bcd", "abcd", "a")

    # Test Case 3: Extra character in the middle
    test_solution("abcdef", "abcdxef", "x")

    # Test Case 4: Both strings are empty except one character in t
    test_solution("", "y", "y")

    # Test Case 5: All characters are the same except one extra
    test_solution("aabbcc", "aabbccd", "d")

    # Test Case 6: Extra character is at the end
    test_solution("xyz", "xyza", "a")

    # Test Case 7: Extra character among repeated characters
    test_solution("ppqq", "pqppqq", "p")

    # Test Case 8: Long strings with random extra character
    test_solution("abcdefghijklmnopqrstuvwxyz",
                  "abcdefghijklmnopqrstuvwxyza", "a")

    # Test Case 9: Mixed characters and extra letter in t
    test_solution("mnoqrst", "mnoqrstu", "u")

    # Test Case 10: Edge case with only one character in both strings
    test_solution("k", "kk", "k")
