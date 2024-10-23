class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1

        left_ptr = len(s) - 1
        right_ptr = len(s) - 1

        while left_ptr >= 0 and s[left_ptr] == " ":
            left_ptr -= 1

        right_ptr = left_ptr

        while left_ptr >= 0 and s[left_ptr] != " ":
            left_ptr -= 1

        return right_ptr - left_ptr


if __name__ == "__main__":
    s = "a "
    solution = Solution()

    print(solution.lengthOfLastWord(s))
