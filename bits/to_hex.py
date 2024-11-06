class Solution:
    def toHex(self, num: int) -> str:

        hashmap = {
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f"
        }

        while num < 1:
            mod = num % 16

            if mod > 9:
                res += hashmap[mod]
            else:
                res += mod

            num = num // 16

        return


def test_solution(num, expected):
    solution = Solution()
    result = solution.toHex(num)
    print(f"Input: num = {num}")
    print(f"Expected: '{expected}', Got: '{result}'")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Positive number
    test_solution(26, "1a")

    # Test Case 2: Zero
    test_solution(0, "0")

    # Test Case 3: Small positive number
    test_solution(15, "f")

    # Test Case 4: Larger positive number
    test_solution(255, "ff")

    # Test Case 5: Negative number within 32-bit range
    test_solution(-1, "ffffffff")

    # Test Case 6: Negative number with multiple digits
    test_solution(-26, "ffffffe6")

    # Test Case 7: Large positive number within 32-bit range
    test_solution(2147483647, "7fffffff")

    # Test Case 8: Edge of 32-bit signed integer range
    test_solution(-2147483648, "80000000")

    # Test Case 9: Mid-range positive number
    test_solution(123456, "1e240")

    # Test Case 10: Random large positive number
    test_solution(305419896, "12345678")
