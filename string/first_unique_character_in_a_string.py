class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1

        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i

        return -1


def test_solution(s, expected):
    solution = Solution()
    result = solution.firstUniqChar(s)
    print(f"Input: s = '{s}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Simple case with unique first character
    test_solution("leetcode", 0)  # 'l' is unique

    # Test Case 2: Unique character in the middle
    test_solution("loveleetcode", 2)  # 'v' is unique

    # Test Case 3: All characters repeated
    test_solution("aabbcc", -1)  # No unique character

    # Test Case 4: Only one character, which is unique
    test_solution("z", 0)

    # Test Case 5: First character is unique
    test_solution("abcdef", 0)  # 'a' is unique

    # Test Case 6: Unique character at the end
    test_solution("aabbccd", 6)  # 'd' is unique

    # Test Case 7: Mixed case with no unique characters
    test_solution("aaabbbccc", -1)

    # Test Case 8: Multiple unique characters, returning the first one
    test_solution("abcabcdd", 6)  # 'd' at index 6 is the first unique

    # Test Case 9: Empty string
    test_solution("", -1)

    # Test Case 10: Long string with unique character late
    test_solution("a"*1000 + "b", 1000)
